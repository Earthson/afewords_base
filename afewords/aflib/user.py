from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *
from emmongodict.emmongodict import EmMongoDict

from bson import ObjectId
from datetime import datetime

from article.about import About
from article.avatar import Avatar

from generator import *

from authority import *


@with_conn
class UserLibDoc(AFDocument):
    __collection__ = 'UserLibDB'

    structure = {
        'drafts_lib' : {
            #objid : objtype
            basestring : basestring,
        },
        'blog_list' : [ObjectId],
        'posted_topic_list' : [ObjectId],
        'favorite_lib' : {
            #objid : objtype
            basestring : basestring,
        },
        'follow_user_lib' : {
            #objid : relation_type
            basestring : basestring,
        },
        'follower_user_lib' : {
            #objid : relation_type
            basestring : basestring,
        },
        'follow_group_lib' : {
            #objid : membership_type
            basestring : basestring,
        },
        'managed_catalog_lib' : dict, #todo Earthson
        'recommended_list' : [(ObjectId, basestring)],
        'notification_list' : list, #todo Earthson
        'tag_lib' : {
            #tagname : blog_id_set
            basestring : [ObjectId],
        },
    }


class UserLib(EmMongoDict):
    datatype = UserLibDoc

    db_info = {
        'db' : 'afewords',
        'collection' : 'UserLibDB',
    }
    @property
    def drafts_lib(self):
        return self.sub_dict('drafts_lib')

    @property
    def favorite_lib(self):
        return self.sub_dict('favorite_lib')

    @property
    def blog_list(self):
        return self.sub_list('blog_list')

    @property
    def posted_topic_list(self):
        return self.sub_list('posted_topic_list')

    @property
    def follow_user_lib(self):
        return self.sub_dict('follow_user_lib')

    @property
    def follower_user_lib(self):
        return self.sub_dict('follower_user_lib')

    @property
    def follow_group_lib(self):
        return self.sub_dict('follow_group_lib')

    @property
    def notification_list(self):
        return self.sub_list('notification_list')

    @property
    def tag_lib(self):
        return self.sub_dict('tag_lib')

    @property
    def managed_catalog_lib(self):
        return self.sub_dict('managed_catalog_lib')


@with_conn
class UserDoc(AFDocument):
    __collection__ = 'UserDB'

    structure = {
        'name' : basestring,
        'alias' : basestring,
        'email' : basestring,
        'sex' : basestring,
        'password' : basestring,
        'token' : basestring,
        'invitations' : int,
        'domain' : basestring,
        'account_status' : basestring,

        'avatar_id' : ObjectId,
        'about_id' : ObjectId,
        'lib_id' : ObjectId,
    }
    required_fields = ['email']
    default_values = {
        'name' : '',
        'alias' : '',
        'sex' : '',
        'password' : '',
        'token' : '',
        'invitations' : 0,
        'domain' : '',
        'account_status' : 'unverified',
        'avatar_id' : Avatar.new_doc,
        'about_id' : About.new_doc,
        'lib_id' : UserLib.new_doc,
    }
    indexes = [
        {
            'fields' : 'email',
            'unique' : True, 
        },
        {
            'fields' : 'domain',
            'unique' : True, 
        }
    ]

@with_mapper
class User(DataBox):
    datatype = UserDoc

    mapper = {
        'name' : True,
        'alias' : True,
        'email' : True,
        'sex' : True,
        'password' : True,
        'token' : True,
        'invitations' : True,
        'domain' : True,
        'account_status' : True,
        'avatar_id' : False,
        'about_id' : False,
        'lib_id' : False,
    }
    own_data =  ['avatar', 'about', 'lib']

    @db_property
    def notice_count():
        def getter(self):
            return len([each for each in self.lib.notification_list.load_all() 
                            if each is not None and each[1] is False])   
        return getter

    @db_property
    def draft_count():
        def getter(self):
            return len(self.lib.drafts_lib.load_all())
        return getter

    @db_property
    def thumb_name():
        def getter(self):
            return self.avatar.thumb_name
        return getter

    @db_property
    def about():
        '''introduction page to user'''
        def getter(self):
            return id_generator(About)(self.data['about_id'])
        return getter

    @db_property
    def avatar():
        def getter(self):
            return id_generator(Avatar)(self.data['avatar_id'])
        return getter

    @db_property
    def lib():
        def getter(self):
            return UserLib(spec={'_id':self.data['lib_id']})
        return getter

    @db_property
    def alltags():
        def getter(self):
            return self.lib.tag_lib['alltags']
        return getter

    @with_user_status
    def authority_verify(self, usr, env=None, **kwargs):
        ret = 0
        if usr == None:
            ret = set_auth(ret, A_READ)
        elif self._id == usr._id:
            ret = set_auth(ret, A_READ | A_WRITE | A_DEL | A_POST)
        return ret

    def post_article(self, article_type, article_obj):
        from article.blog import Blog
        from article.comment import Comment
        a_mapper = {
            Blog.__name__ : self.post_blog,
            Comment.__name__ : self.post_comment,
        }
        return a_mapper[article_type](article_obj)

    def post_blog(self, blogobj):
        #from article.blog import Blog
        blogid = blogobj._id
        del self.lib.drafts_lib[blogid]
        self.lib.blog_list.push(blogid)
        blogobj.do_post()
        for each in blogobj.tag:
            tmp = self.tag_lib[each]
            if tmp is None:
                tmp = []
            tmp = set(tmp)
            tmp.add(blogobj._id)
            self.tag_lib[each] = list(tmp)

    def post_topic(self, topicobj, group):
        topicid = topicobj._id
        group.accept_topic(self, topicobj)
        self.drafts_lib.remove_obj(topicid)
        self.posted_topic_list.push(topicid)
        topicobj.do_post()

    def post_feedback(self, feedbackobj, group):
        group.accept_feedback(self, feedbackobj)
        self.drafts_lib.remove_obj(feedbackobj._id)
        feedbackobj.do_post()

    def delete_blog(self, blogobj):
        blogid = blogobj._id
        self.blog_list.pull(blogid)
        for each in blogobj.tag:
            self.remove_from_tag(blogobj, each)

    def add_to_tag(self, blogobj, tagname):
        blogobj.add_to_tag(tagname)
        tagmem = self.lib.tag_lib[tagname]
        if tagmem is None:
            self.lib.tag_lib[tagname] = []
            tagmem = []
        tagmem = set(tagmem)
        tagmem.add(str(blogobj._id))
        self.lib.tag_lib[tagname] = list(tagmem)

    def remove_from_tag(self, blogobj, tagname):
        blogobj.remove_from_tag(tagname)
        tagmem = self.lib.tag_lib[tagname]
        if tagmem is not None:
            tagmem = set(tagmem)
            tagmem.discard(str(blogobj._id))
            self.lib.tag_lib[tagname] = list(tagmem)

    def add_tags(self, new_tags):
        new_tags = set(new_tags)
        if not new_tags.issubset(set(self.alltags)):
            all_tags = set(self.alltags) | new_tags
            self.lib.tag_lib['alltags'] = list(all_tags)

    def remove_tags(self, rm_tags):
        rm_tags = set(rm_tags)
        self.lib.tag_lib['alltags'] = list(set(self.alltags) - rm_tags)

    def with_new_tags(self, blogobj, new_tags):
        old_tags = set(blogobj.tag)
        new_tags = set(new_tags) & set(self.alltags)
        for each in old_tags - new_tags:
            self.remove_from_tag(blogobj, each)
        for each in new_tags - old_tags:
            self.add_to_tag(blogobj, each)

    def blogs_from_tag(self, tagname):
        from article.blog import Blog
        if not tagname:
            return
        ans = Blog.by_ids(self.lib.tag_lib[tagname])
        #ans = [Blog.by_id(each) for each in self.lib.tag_lib[tagname]]
        if ans:
            self.lib.tag_lib.sub_list(tagname).set_all([each._id 
                                                    for each in ans])
            #self.lib.tag_lib[tagname] = [each._id for each in ans]
        return ans

    def blogs_info_view_by(self, usr=None, tagname=None):
        from article.blog import Blog
        if tagname:
            toview = self.blogs_from_tag(tagname)
            toview.sort()
        else:
            toview = self.blogs
        if usr: 
            return [usr.as_viewer_to_article_info(each.basic_info) 
                        for each in toview]
        return [each.basic_info for each in toview]

    def post_status(self, statusobj):
        statusid = statusobj._id
        self.drafts_lib.remove_obj(statusid)
        self.status_list.push(statusid)
        statusobj.do_post()

    def post_comment(self, commentobj):
        father = generator(commentobj.father_id, commentobj.father_type)
        self.drafts_lib.remove_obj(commentobj._id)
        father.comment_list.push(commentobj._id)
        commentobj.do_post()

    def follow_user(self, usr):
        self.follow_user_lib.add_obj(usr)
        usr.follower_user_lib.add_obj(self)

    def unfollow_user(self, usr):
        self.follow_user_lib.remove_obj(usr._id)
        usr.follower_user_lib.remove_obj(self._id)

    def follow_group(self, group):
        status = group.accept_user(self)
        if status:
            self.follow_group_lib.update(**{str(group._id):datetime.now()})

    def unfollow_group(self, group):
        group.remove_user(self)
        self.follow_group_lib.pop(str(group._id))
        self.managed_group_lib.pop(str(group._id))

    def accept_group_management(self, group):
        self.managed_group_lib.update(**{str(group._id):datetime.now()})

    def cancel_group_management(self, group):
        self.managed_group_lib.pop(str(group._id))

    def like_post(self, obj):
        if self.favorite_lib[str(obj._id)] is not None:
            return None
        self.favorite_lib.add_obj(obj)
        obj.statistics.like_count += 1

    def dislike_post(self, obj):
        if self.favorite_lib[str(obj._id)] is None:
            return None
        self.favorite_lib.remove_obj(obj._id)
        obj.statistics.like_count -= 1

    def is_follow(self, other_id):
        '''self follows other?'''
        return str(other_id) in self.lib.follow_user_lib

    def is_follower(self, other_id):
        '''other is self's follower?'''
        return str(other_id) in self.lib.follower_user_lib

    def as_viewer(self, other):
        '''as viewer, update user infomation dict'''
        user_info = other.basic_info
        user_info['isfollow'] = self.is_follow(user_info['uid'])
        user_info['isme'] = (self.uid == user_info['uid'])
        return user_info

    def as_viewer_to_uinfo(self, uinfo):
        uinfo['isfollow'] = self.is_follow(uinfo['uid'])
        uinfo['isme'] = (self.uid == uinfo['uid'])
        return uinfo

    def as_viewer_to_article_info(self, ainfo):
        ainfo['author']['isfollow'] = self.is_follow(ainfo['author']['uid'])
        ainfo['author']['isme'] = (self.uid == ainfo['author']['uid'])
        return ainfo

    def is_like(self, obj):
        return obj.uid in self.lib.favorite_lib

    #property for page&json
    @db_property
    def notify_user_info():
        def getter(self):
            attrs = ['uid', 'name', 'draft_count', 
                        'notice_count', 'thumb_name']
            ans = dict()
            ans['uid'] = self.uid
            ans['name'] = self.name
            ans['draft_count'] = self.draft_count
            ans['notice_count'] = self.notice_count
            ans['thumb'] = self.thumb_name
            return ans
        return getter

    @db_property
    def basic_info():
        '''for follow/follower display'''
        def getter(self):
            ans = dict()
            ans['uid'] = self.uid
            ans['name'] =self.name
            ans['thumb'] = self.thumb_name
            ans['isfollow'] = False
            ans['isme'] = False
            ans['tag_list'] = self.alltags
            return ans
        return getter

    @db_property
    def followers():
        '''users followed self'''
        def getter(self):
            follower_ids = self.lib.follower_user_lib.load_all().keys()
            return self.by_ids(follower_ids)
        return getter

    @db_property
    def follows():
        '''users self followed'''
        def getter(self):
            follow_ids = self.lib.follow_user_lib.load_all().keys()
            return self.by_ids(follow_ids)
        return getter

    @db_property
    def blogs():
        from article.blog import Blog
        def getter(self):
            ids = self.lib.blog_list.load_all()
            ans = Blog.by_ids(ids)
            self.lib.blog_list.set_all([each._id for each in ans])
            return ans
        return getter

    @db_property
    def as_env():
        def getter(self):
            ans = dict()
            ans['type'] = self.__class__.__name__
            ans['entity'] = self.basic_info
            return ans
        return getter
