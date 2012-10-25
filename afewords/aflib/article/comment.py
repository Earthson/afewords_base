from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *
from emmongodict.emmongodict import EmMongoDict
from databox.mongokit_utils import with_conn

from article import ArticleDoc, Article

from bson import ObjectId


@with_conn
class CommentDoc(ArticleDoc.__clsobj__):
    __collection__ = 'CommentDB'

    structure = {
        'ref_comment_id': ObjectId,
        'ref_comment_info' : basestring,
    }
    default_values = {
        'ref_comment_id' : None,
        'ref_comment_info' : None,
    }


from authority import *

@with_mapper
class Comment(Article):
    datatype = CommentDoc

    mapper = {
        'ref_comment_id' : True,
        'ref_comment_info' : False,
    }

    @with_user_status
    def authority_verify(self, usr, env=None, **kwargs):
        ret = Article.authority_verify(self, usr, env, **kwargs)
        if usr._id == self.father_id:
            ret |= A_DEL
        return ret

    def set_by_info(self, infodoc):
        ans = dict()
        ans['body'] = infodoc['body']
        self.set_propertys(**ans)
        
    @db_property
    def ref_comment():
        def getter(self):
            return Comment.by_id(self.data['ref_comment_id'])
        def setter(self, value):
            if value:
                self.data['ref_comment_id'] = value._id
                self.data['ref_comment_info'] = value.short_article_ref_info
            else:
                self.data['ref_comment_id'] = None
                self.data['ref_comment_info'] = None
        return getter, setter


    #property for json
    @db_property
    def comment_info_for_json():
        def getter(self):
            ans = dict()
            ans['aid'] = self.uid
            ans['content'] = self.view_body
            ans['release_time'] = str(self.release_time)
            ans['author'] = self.author.basic_info_for_json
            ans['permission'] = 'r'
            ans['ref_comment_info'] = self.ref_comment_info
            return ans
        return getter
