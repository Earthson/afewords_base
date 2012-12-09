from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *
from emmongodict.emmongodict import EmMongoDict

from bson import ObjectId
from datetime import datetime

from article import * #try init all article packages
from article.about import About
from article.avatar import Avatar
from article.blog import Blog

from userstat import UserStat, UserStatMongo

from generator import *

from authority import *

from operator import itemgetter, attrgetter




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
            #objid : [objtype, timein],
            basestring : [basestring, datetime],
        },
        'follow_user_lib' : {
            #objid : [relation_type, timeadd]
            basestring : [basestring, datetime],
        },
        'follower_user_lib' : {
            #objid : [relation_type, timeadd]
            basestring : [basestring, datetime],
        },
        'follow_group_lib' : {
            #objid : [membership_type, timadd]
            basestring : [basestring, datetime],
        },
        'managed_catalog_lib' : {
            #objid : [membership_type(admin/owner), timeadd]
            basestring : [basestring, datetime],
        },
        'recommended_list' : [(ObjectId, basestring)], #[id, type]
        'notification_lib' : {
            #noti_id
            basestring : {
                'info' : basestring, #info to show
                'isread' : bool, #have read?
            }
        }, 
        'tag_lib' : {
            #tagname : [[blog_id, releasetime]]
            basestring : [[ObjectId, datetime]],
        },
    }


class UserLib(EmMongoDict):
    datatype = UserLibDoc

    db_info = {
        'db' : 'afewords',
        'collection' : 'UserLibDB',
    }

    @property
    def own_data(self):
        ans = list()
        ans += [each for each in list_generator( [(ek, ev[0]) 
                    for ek, ev in self.drafts_lib.items()]) 
                if each is not None]
        ans += Blog.by_ids(self.blog_list.load_all())
        return ans

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
    def notification_lib(self):
        return self.sub_dict('notification_lib')

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
        'account_status' : basestring, #unverified, normal, limited 
        'release_time' : datetime,

        'avatar_id' : ObjectId,
        'about_id' : ObjectId,
        'lib_id' : ObjectId,
        'userstat_id' : ObjectId,
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
        'about_id' : None,
        'lib_id' : UserLib.new_doc,
        'release_time' : datetime.now,
        'userstat_id' : UserStat.new_doc,
    }
    indexes = [
        {
            'fields' : 'email',
            'unique' : True, 
        },
        {
            'fields' : 'domain',
            'unique' : True, 
        },
        {
            'fields' : 'name',
            'unique' : False,
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
        'release_time' : True,
        'avatar_id' : False,
        'about_id' : False,
        'lib_id' : False,
        'userstat_id' : False,
    }
    own_data =  ['avatar', 'about', 'lib', 'stat_info']

    def __init__(self, data=None, *args, **kwargs):
        DataBox.__init__(self, data, *args, **kwargs)
        if data is None:
            self.domain = self.uid
            self.about.set_propertys(env=self, author_id=self._id)

    def remove(self):
        '''just log off'''
        self.logoff()

    def logoff(self):
        self.account_status = 'logoff'

    @db_property
    def notice_count():
        def getter(self):
            ans = self.lib.notification_lib.values()
            return len([each for each in ans if each['isread'] is False])
        return getter

    @db_property
    def draft_count():
        def getter(self):
            return len(self.lib.drafts_lib.load_all())
        return getter

    @db_property
    def stat_info():
        '''user statistics info'''
        def getter(self):
            return UserStat.by_id(self.data['userstat_id'])
        return getter

    @db_property
    def stat_info_doc():
        '''user statistics info'''
        def getter(self):
            return UserStatMongo.by_id(self.data['userstat_id'])
        return getter

    @db_property
    def about():
        '''introduction page to user'''
        def getter(self):
            ans = About.by_id(self.data['about_id'])
            if ans is None:
                ans = About()
                self.data['about_id'] = ans._id
                ans.set_propertys(author_id=self._id, env=self)
                return ans, True
            if not ans.author_id or not ans.env_id or not ans.env_type:
                ans.set_propertys(author_id=self._id, env=self)
            return ans
        return getter

    @db_property
    def avatar():
        def getter(self):
            return Avatar.by_id(self.data['avatar_id'])
        return getter

    @db_property
    def lib():
        def getter(self):
            return UserLib(spec={'_id':self.data['lib_id']})
        return getter

    @db_property
    def alltags():
        def getter(self):
            ans = self.lib.tag_lib['alltags']
            if ans is None:
                return list()
            return ans
        return getter

    @with_user_status
    def authority_verify(self, usr=None, env=None, **kwargs):
        ret = 0
        if usr is None:
            ret = set_auth(ret, A_READ)
        elif self._id == usr._id:
            ret = set_auth(ret, A_READ | A_WRITE | A_DEL | A_POST | A_OWNER)
        return ret

    def accept_notification(self, info, from_who=None):
        import time
        noti_id = repr(time.time()).replace('.', '#') #generate noti_id
        doc = {
            'info' : info,
            'isread' : False,
        }
        if from_who.uid != self.uid:
            self.lib.notification_lib[noti_id] = doc

    @db_property
    def notifications():
        def getter(self):
            ans = dict([(ek, {
                'index' : ek,
                'content' : ev['info'],
                'isread' : ev['isread'],
            }) for ek, ev in self.lib.notification_lib.items()])
            noti_ids = [ek for ek, ev in ans.items()]
            noti_ids = sorted(noti_ids, reverse=True)
            return [ans[each] for each in noti_ids]
        return getter

    def read_notifications(self, *noti_ids):
        noti_lib = self.lib.notification_lib
        for each in noti_ids:
            if each in noti_lib:
                noti_lib.sub_dict(each)['isread'] = True

    def remove_notifications(self, *noti_ids):
        noti_lib = self.lib.notification_lib
        for each in noti_ids:
            del noti_lib[each]

    def read_all_notifications(self):
        noti_lib = self.lib.notification_lib
        noti_all = noti_lib.load_all()
        for each in noti_all.keys():
            noti_all[each]['isread'] = True
        noti_lib.set_all(noti_all)

    def empty_notifications(self):
        noti_lib = self.lib.notification_lib
        noti_lib.set_all(dict())

    def add_to_drafts(self, obj):
        self.lib.drafts_lib[obj.uid] = obj.__class__.__name__

    def post_article(self, article_type, article_obj):
        from article.blog import Blog
        from article.comment import Comment
        from article.about import About
        a_mapper = {
            Blog.cls_name : self.post_blog,
            Comment.cls_name : self.post_comment,
            About.cls_name : self.post_normal_article,
        }
        return a_mapper[article_type](article_obj)

    def post_normal_article(self, article_obj):
        aid = article_obj.uid
        article_obj.do_post()
        del self.lib.drafts_lib[aid]

    def post_blog(self, blogobj):
        blogid = blogobj.uid
        self.lib.blog_list.push(blogobj._id)
        blogobj.do_post()
        del self.lib.drafts_lib[blogid]
        for each in blogobj.tag:
            self.lib.tag_lib.sub_list(each).add_to_set(
                                [blogobj._id, blogobj.release_time])

    def post_comment(self, commentobj):
        commentid = commentobj.uid
        father = generator(commentobj.father_id, commentobj.father_type)
        father.lib.comment_list.push(commentobj._id)
        commentobj.do_post()
        del self.lib.drafts_lib[commentid]

    def post_topic(self, topicobj, group):
        topicid = topicobj.uid
        group.accept_topic(self, topicobj)
        self.drafts_lib.remove_obj(topicid)
        self.posted_topic_list.push(topicid)
        topicobj.do_post()

    def post_feedback(self, feedbackobj, group):
        group.accept_feedback(self, feedbackobj)
        self.drafts_lib.remove_obj(feedbackobj._id)
        feedbackobj.do_post()

    def delete_blog(self, blogobj):
        blogid = blogobj.uid
        self.blog_list.pull(blogid)
        for each in blogobj.tag:
            self.remove_from_tag(blogobj, each)

    def add_to_tag(self, blogobj, tagname):
        blogobj.add_to_tag(tagname)
        tag_blogs = self.lib.tag_lib.sub_list(tagname)
        tag_blogs.add_to_set([blogobj._id, blogobj.release_time])

    def remove_from_tag(self, blogobj, tagname):
        blogobj.remove_from_tag(tagname)
        tag_blogs = self.lib.tag_lib.sub_list(tagname)
        tag_blogs.pull([blogobj._id, blogobj.release_time])

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

    def blogs_from_tag(self, tagname, vfrom=0, vlim=20):
        from article.blog import Blog
        if not tagname:
            return [], 0
        tag_blogs = self.lib.tag_lib.sub_list(tagname)
        toview = tag_blogs.load_all()
        if toview is None:
            toview = []
        toview = sorted(toview, key=itemgetter(1), reverse=True)
        len_toview = len(toview)
        if vfrom >= len_toview:
            return [], len_toview
        if vfrom + vlim > len_toview:
            vlim = len_toview - vfrom
        toview = [tuple(each) for each in toview[vfrom:(vfrom+vlim)]]
        tmp = set(toview)
        toview = Blog.by_ids([each[0] for each in toview])
        toview.sort()
        tmp2 = set((each._id, each.release_time) for each in toview)
        tag_blogs.pull(*tuple(tmp - tmp2)) #try remove blog not existed
        return toview, len_toview

    @db_property
    def drafts_info():
        '''basic article info for drafts'''
        def getter(self):
            draft_lib = self.lib.drafts_lib
            tmp = draft_lib.items()
            drafts = list_generator(tmp)
            for i in xrange(len(tmp)):
                if drafts[i] is None:
                    del draft_lib[tmp[i][0]]
            return [each.obj_info_view_by('basic_info', self) 
                        for each in drafts if each]
        return getter

    def fav_info_view_by(self, usr=None, vfrom=0, vlim=20):
        fav_all = [(ek, ev[0], ev[1])
                for ek, ev in usr.lib.favorite_lib.load_all().iteritems()]
        fav_all = sorted(fav_all, key=lambda it: it[2], reverse=True)
        toview = [each[0:2] for each in fav_all]
        len_toview = len(toview)
        if vfrom > len_toview:
            return [], len_toview
        if vfrom + vlim > len_toview:
            vlim = len_toview - vfrom
        toview = toview[vfrom:(vfrom+vlim)]
        tmp = set([each[0] for each in toview])
        toview = [each for each in list_generator(toview) if each]
        tmp2 = set([each.uid for each in toview])
        self.lib.favorite_lib.delete_propertys(tuple(tmp - tmp2))
        return [each.obj_info_view_by('overview_info', usr, env=usr) 
                    for each in toview], len_toview

    def blogs_info_view_by(self, usr=None, tagname=None, vfrom=0, vlim=20):
        from article.blog import Blog
        if tagname and tagname != 'default':
            toview, len_toview = self.blogs_from_tag(tagname, vfrom, vlim)
        else:
            toview = self.blogids
            len_toview = len(toview)
            if vfrom > len_toview:
                return [], len_toview
            if vfrom + vlim > len_toview:
                vlim = len_toview - vfrom
            toview = toview[vfrom:(vfrom+vlim)]
            tmp = set(toview)
            toview = Blog.by_ids(toview)
            toview.sort()
            tmp2 = set(each._id for each in toview)
            self.lib.blog_list.pull(*tuple(tmp - tmp2)) 
            #try remove item not exist
        return [each.obj_info_view_by('basic_info', usr, env=usr) 
                        for each in toview], len_toview

    def post_status(self, statusobj):
        statusid = statusobj._id
        self.drafts_lib.remove_obj(statusid)
        self.status_list.push(statusid)
        statusobj.do_post()

    def follow_user(self, usr):
        val = ['normal', datetime.now()]
        self.lib.follow_user_lib[usr.uid] = val
        usr.lib.follower_user_lib[self.uid] = val
        return True

    def unfollow_user(self, usr):
        del self.lib.follow_user_lib[usr.uid]
        del usr.lib.follower_user_lib[self.uid]
        return True

    def follow_group(self, group):
        status = group.accept_user(self)
        if status:
            self.follow_group_lib.update(**{str(group._id):datetime.now()})

    def unfollow_group(self, group):
        group.remove_user(self)
        self.follow_group_lib.pop(str(group._id))
        self.managed_group_lib.pop(str(group._id))

    def create_catalog(self, name, keywords=''):
        from article.catalog import Catalog
        newobj = Catalog(attrs={'name':name, 'keywords':keywords, 'owner':self})
        self.lib.managed_catalog_lib[newobj.uid] = ['admin', datetime.now()]
        return newobj

    def accept_catalog_management(self, catalog_obj):
        '''call from catalog_obj by catalog_obj.add_manager'''
        mclib = self.lib.managed_catalog_lib
        if catalog_obj.uid in mclib:
            return True
        mclib[catalog_obj.uid] = ['admin', datetime.now()]
        return True

    def cancel_catalog_management(self, catalog_obj):
        '''call from catalog_obj by catalog_obj.remove_manager'''
        pass #todo Earthson

    def accept_group_management(self, group):
        self.lib.managed_group_lib.update(**{str(group._id):datetime.now()})

    def cancel_group_management(self, group):
        self.lib.managed_group_lib.pop(str(group._id))

    def like_post(self, obj):
        '''do not call this method. call reverse_like_post instead'''
        fav_lib = self.lib.favorite_lib
        fav_lib[obj.uid] = [obj.cls_name, datetime.now()]
        obj.statistics.like_count += 1

    def dislike_post(self, obj):
        '''do not call this method. call reverse_like_post instead'''
        fav_lib = self.lib.favorite_lib
        del fav_lib[obj.uid]
        obj.statistics.like_count -= 1

    def reverse_like_post(self, obj):
        '''reverse like state. like->dislike, dislike->like'''
        from article.article import Article
        from article.catalog import Catalog
        if not isinstance(obj, Article) and not isinstance(obj, Catalog):
            return False
        if obj.uid in self.lib.favorite_lib:
            self.dislike_post(obj)
        else:
            self.like_post(obj)
        return True

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
        if not uinfo:
            return None
        uinfo['isfollow'] = self.is_follow(uinfo['uid'])
        uinfo['isme'] = (self.uid == uinfo['uid'])
        return uinfo

    def obj_info_view_by(self, info_name='basic_info',
                        usr=None, env=None, **kwargs):
        uinfo = self.get_propertys(info_name)[0]
        uinfo['permission'] = auth_str(self.authority_verify(
                        usr, env, **kwargs))
        if usr is None:
            return uinfo
        uinfo['isfollow'] = usr.is_follow(self.uid)
        uinfo['isme'] = (self.uid == usr.uid)
        return uinfo

    def json_info_view_by(self, info_name='overview',
                        usr=None, env=None, **kwargs):
        ans = dict()
        ans['uid'] = self.uid
        ans['name'] = self.name
        ans['thumb'] = self.avatar.thumb_url
        return ans
        

    def is_like(self, obj):
        return obj.uid in self.lib.favorite_lib

    #property for page&json
    @db_property
    def notify_user_info():
        def getter(self):
            ans = dict()
            ans['uid'] = self.uid
            ans['name'] = self.name
            ans['draft_count'] = self.draft_count
            ans['notice_count'] = self.notice_count
            ans['thumb'] = self.avatar.thumb_url
            ans['account_status'] = self.account_status
            return ans
        return getter

    @db_property
    def basic_info():
        '''for follow/follower display'''
        def getter(self):
            return self.as_env_info
        return getter

    @db_property
    def basic_info_for_json():
        def getter(self):
            return self.as_env_info
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
    def blogids():
        from article.blog import Blog
        def getter(self):
            return self.lib.blog_list.load_all()[::-1]
        return getter

    @db_property
    def as_env_info():
        def getter(self):
            ans = dict()
            ans['uid'] = self.uid
            ans['name'] = self.name
            ans['thumb'] = self.avatar.thumb_url
            ans['isfollow'] = False
            ans['isme'] = False
            ans['tag_list'] = self.alltags
            ans['account_status'] = self.account_status
            return ans
        return getter

    @db_property
    def overview_info():
        def getter(self):
            ans = dict()
            ans['uid'] = self.uid
            ans['name'] = self.name
            ans['thumb'] = self.avatar.thumb_url
            ans['url'] = self.obj_url
            ans['isfollow'] = False
            ans['isme'] = False
            return ans
        return getter

    @db_property
    def as_env():
        def getter(self):
            ans = dict()
            ans['env_type'] = self.cls_name
            ans['env_id'] = self.uid
            ans['entity'] = self.as_env_info
            return ans
        return getter

    @db_property
    def managed_catalogs():
        def getter(self):
            from article.catalog import Catalog
            cids = self.lib.managed_catalog_lib.keys()
            return sorted(Catalog.by_ids(cids), reverse=True)
        return getter
