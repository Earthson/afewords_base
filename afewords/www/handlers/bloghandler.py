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
        if userstat.view_article(blog_to):
            blog_to.statistics.view_count += 1
        if usr:
            page['islike'] = usr.is_like(blog_to)
        page.render()
        return
