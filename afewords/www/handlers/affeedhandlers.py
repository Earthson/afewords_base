#coding=utf-8

from basehandler import *
from pages.af_feedpage import *

from article.blog import Blog
from global_info import recent_blogs

class AFFeedPageHandler(BaseHandler):
    def get(self):
        handler_page = AFFeedPage(self)
        handler_page.render()
        return #0

class AFBlogsRecentHandler(BaseHandler):
    def post(self):
        handler_page = AFFeedPage(self)
        usr = self.current_user
        try:
            blogs = sorted(Blog.by_ids(recent_blogs.get_slice(-20)),
                                reverse=True)
        except:
            blogs = []
        handler_page['feed_list'] = [each.obj_info_view_by('basic_info',
                usr=usr, env=None) for each in blogs]
        handler_page.render()
        return #0


class AFUserFavHandler(BaseHandler):
    '''usr's favorites'''
    @with_login
    def get(self):
        handler_page = AFFeedLikePage(self)
        usr = self.current_user
        #todo Earthson
        handler_page.render()
        return #0
