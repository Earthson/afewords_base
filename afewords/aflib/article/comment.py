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


class Comment(Article):
    datatype = CommentDoc


    def set_by_info(self, infodoc):
        Article.set_by_info(self, infodoc)
        self.ref_comments = infodoc['ref_comments']
        
    @db_property
    def ref_comments():
        def getter(self):
            return self.data['ref_comments']
        def setter(self, value):
            self.data['ref_comments'] = value
        return getter, setter

    #property for page&json
    @db_property
    def comment_info():
        def getter(self):
            ans = dict()
            ans['aid'] = self.uid
            ans['content'] = self.view_body
            ans['release_time'] = str(self.release_time)
            ans['author'] = self.author.basic_info_for_json
            ans['ref_comment_list'] = self.ref_comments
            return ans
        return getter
