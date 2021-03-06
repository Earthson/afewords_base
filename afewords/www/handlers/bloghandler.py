#coding=utf-8

from basehandler import *
from pages.pages import BlogPage


class BlogHandler(BaseHandler):

    def get(self, bid):
        from article.blog import Blog
        usr = self.current_user
        userstat = self.userstat
        blog_to = Blog.by_id(bid)
        if(blog_to is None): 
            return self.send_error(404);
        preview = self.get_esc_arg('preview', 'no')
        page = BlogPage(self)
        page['ispreview'] = True if preview == 'yes' else False
        page['article'] = blog_to.obj_info_view_by('view_info', 
                    usr=usr, env=usr)
        if preview != 'yes' and userstat.view_article(blog_to):
            blog_to.statistics.view_count += 1
        page['islike'] = False if usr is None else usr.is_like(blog_to)
        page['title'] = page['article']['title'] + u' - 子曰博文'
        page['meta_keywords'] = page['article']['keywords']
        page['description'] = page['article']['title']
        page.render()
        return
