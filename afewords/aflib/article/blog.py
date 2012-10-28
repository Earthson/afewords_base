from databox.mongokit_utils import with_conn

from article import ArticleDoc, Article


@with_conn
class BlogDoc(ArticleDoc.__clsobj__):
    __collection__ = 'BlogDB'


class Blog(Article):
    datatype = BlogDoc

    @db_property
    def obj_url():
        def getter(self):
            return self.main_url + 'blog/' + self.uid
