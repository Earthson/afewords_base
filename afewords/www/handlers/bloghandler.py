#coding=utf-8

from basehandler import *
from pages.pages import BlogPage


class BlogHandler(BaseHandler):

    def get(self, bid):
        from article.blog import Blog
        usr = self.current_user
        blog_to = Blog.by_id(bid)
        print bid
        print blog_to
        if(blog_to is None): 
            return self.send_error(404);
        preview = self.get_esc_arg('preview', 'no')
        page = BlogPage(self)
        page['ispreview'] = True if preview == 'yes' else False
        page['article'] = blog_to.view_info
        if usr:
            page['article']['author'] = usr.as_viewer(blog_to.author)
            page['islike'] = usr.is_like(blog_to)
        #print page['article']['author']
        page.render()
        return
