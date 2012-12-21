#coding=utf-8
'''
RSS/Atom Feed service
'''

from basehandler import *
from article.blog import Blog
from global_info import recent_blogs
from user import User

from pages.feedpages import ArticleFeedRender

from pages.feedpages import AtomRecentBlogPage

class AtomRecentHandler(BaseHandler):
    def get(self):
        handler_page = AtomRecentBlogPage(self)
        blogs = sorted(Blog.by_ids(recent_blogs.get_slice(-10)))
        atominfos = [each.atom_info for each in blogs]
        handler_page.add_entries(*atominfos)
        handler_page.init_page()
        handler_page.render()
        return #0

from pages.feedpages import AtomUserBlogPage

class AtomUserBlogHandler(BaseHandler):
    def get(self, uid):
        handler_page = AtomUserBlogPage(self)
        usr = User.by_id(uid)
        if usr is not None:
            handler_page.update(**usr.blog_atom_info)
        handler_page.init_page()
        handler_page.render()
        return #0

from pages.feedpages import RSSRecentBlogPage

class RSSRecentHandler(BaseHandler):
    def get(self):
        handler_page = RSSRecentBlogPage(self)
        blogs = sorted(Blog.by_ids(recent_blogs.get_slice(-10)))
        handler_page['items'] = [each.rss_info for each in blogs]
        handler_page.init_page()
        handler_page.render()
        return #0


from pages.feedpages import RSSUserBlogPage

class RSSUserBlogHandler(BaseHandler):
    def get(self, uid):
        handler_page = RSSUserBlogPage(self)
        usr = User.by_id(uid)
        if usr is not None:
            handler_page.update(**usr.blog_rss_info)
        handler_page.init_page()
        handler_page.render()
        return #0

