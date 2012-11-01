from databox.mongokit_utils import with_conn
from databox.databox import *

from article import ArticleDoc, Article


@with_conn
class BlogDoc(ArticleDoc.__clsobj__):
    __collection__ = 'BlogDB'

@with_mapper
class Blog(Article):
    datatype = BlogDoc

    @db_property
    def obj_url():
        def getter(self):
            return self.main_url + 'blog/' + self.uid
        return getter
    
    def do_post(self):
        from global_info import recent_blogs
        Article.do_post(self)
        recent_blogs.push(self._id)
        recent_blogs.pop_head()
