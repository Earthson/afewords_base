from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *
from emmongodict.emmongodict import EmMongoDict
from databox.mongokit_utils import with_conn

from article import ArticleDoc, Article


@with_conn
class CommentDoc(ArticleDoc.__clsobj__):
    __collection__ = 'CommentDB'

    structure = {
        'ref_comments': list,
    }
    default_values = {
        'ref_comments': list,
    }


from authority import *

class Comment(Article):
    datatype = CommentDoc

    @with_user_status
    def authority_verify(self, usr, env=None, **kwargs):
        ret = Article.authority_verify(self, usr, env, **kwargs)
        if usr._id == self.father_id:
            ret |= A_DEL
        return ret

    def set_by_info(self, infodoc):
        Article.set_by_info(self, infodoc)
        self.ref_comments = infodoc['ref_comments']
        
    @db_property
    def ref_comments():
        def getter(self):
            return Comment.by_ids(self.data['ref_comments'])
        def setter(self, value):
            self.data['ref_comments'] = value
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
            try:
                ans['ref_comment'] = self.ref_comments[0].short_article_ref
            except:
                ans['ref_comment'] = None
            return ans
        return getter
