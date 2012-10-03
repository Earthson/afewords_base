from databox.mongokit_utils import with_conn

from article import ArticleDoc, Article


@with_conn
class CommentDoc(ArticelDoc.__clsobj__):
    __collection__ = 'CommentDB'

    structure = {
        'ref_comments': list,
    }
    default_values = {
        'ref_comments': list,
    }


class Comment(Article):
    datatype = CommentDoc

    @db_property
    def ref_comments():
        def getter(self):
            return self.data['ref_comments']
        def setter(self, value):
            self.data['ref_comments'] = value
        return getter, setter
