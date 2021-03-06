#coding=utf-8

from basehandler import *
from pages.af_feedpage import *

from article.blog import Blog
from global_info import recent_blogs
from user import User

class AFFeedPageHandler(BaseHandler):
    def get(self):
        handler_page = AFFeedPage(self)
        handler_page.render()
        return #0

class AFBlogsRecentHandler(BaseHandler):
    def get(self):
        handler_page = AFFeedPage(self)
        usr = self.current_user
        try:
            blogs = sorted(Blog.by_ids(recent_blogs.get_slice(-10)))
        except:
            blogs = []
        handler_page['id_list'] = [str(each)+'##blog' for each in 
                    (recent_blogs.load_all()[100:-10][::-1]) if each]
        handler_page['feed_list'] = [each.obj_info_view_by('basic_info',
                usr=usr, env=None) for each in blogs]
        handler_page.render()
        return #0


class AFUserFavPara(BaseHandlerPara):
    doc = {
        'page' : 1,
    }

    def read(self):
        try:
            self['page'] = int(self.handler.get_esc_arg('page', self['page']))
        except:
            self['page'] = 1


class AFUserFavHandler(BaseHandler):
    '''usr's favorites'''
    @with_login
    def get(self):
        from generator import list_generator
        handler_para = AFUserFavPara(self)
        handler_page = AFFeedLikePage(self)
        usr = self.current_user
        handler_page['current_page'] = handler_para['page']
        enum = 10
        handler_page['like_list'], like_cnt = usr.fav_info_view_by(usr,
                    vfrom=enum*(handler_para['page'] - 1), vlim=enum) 
        handler_page['page_all'] = (like_cnt-1)//enum + 1
        paradoc = dict()
        #para need to be add. 
        handler_page['urlparas'] = paradoc
        handler_page['baseurl'] = self.request_url
        handler_page.page_init()
        handler_page.render()
        return #0

class AFUserBlogLibPara(BaseHandlerPara):
    paradoc = {
        'page' : 1,
        'tag' : 'default',
    }
    def read(self):
        try:
            self['page'] = int(self.handler.get_esc_arg('page', self['page']))
        except:
            self['page'] = 1
        self['tag'] = self.handler.get_esc_arg('tag', self['tag'])


class AFUserBlogLibHandler(BaseHandler):
    @with_login
    def get(self):
        handler_para = AFUserBlogLibPara(self)
        handler_page = AFFeedMyselfPage(self)
        usr = self.current_user
        handler_page['current_page'] = handler_para['page']
        handler_page['tag_list'] = usr.alltags
        handler_page['current_tag'] = handler_para['tag']
        enum = 10
        handler_page['blog_list'], blog_cnt = usr.blogs_info_view_by(usr, 
                handler_page['current_tag'], 
                vfrom=enum*(handler_para['page'] - 1), vlim=enum)
        handler_page['page_all'] = (blog_cnt-1)//enum + 1
        #for pagin support
        paradoc = dict()
        if handler_para['tag'] != 'default':
            paradoc['tag'] = handler_para['tag']
        handler_page['urlparas'] = paradoc
        handler_page['baseurl'] = self.request_url
        handler_page.page_init()
        handler_page.render()
        return
