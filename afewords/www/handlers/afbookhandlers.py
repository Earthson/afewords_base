#coding=utf-8

from basehandler import *
from pages.af_bookpage import *

from article.catalog import Catalog
from global_info import recent_books

class AFBookHandler(BaseHandler):
    def get(self):
        handler_page = AFBookPage(self)
        usr = self.current_user
        try:
            books = sorted(Catalog.by_ids(recent_books.get_slice(-20)), 
                                reverse=True)
        except:
            books = []
        handler_page['book_list'] = [each.obj_info_view_by('overview_info',
                usr=usr, env=None) for each in books]
        handler_page.render()
        return #0

class AFUserBookPara(BaseHandlerPara):
    paradoc = {
        'id': '1',
        'type': 'info', # 'info', 'about', 'catalog', 'invite'
    }
    

class AFUserBookHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = AFBookMyselfPage(self)
        usr = self.current_user
        books = usr.managed_catalogs
        handler_page['book_list'] = [each.obj_info_view_by('overview_info',
                usr=usr, env=None) for each in books]
        handler_page.render()
        return #0


class AFBookCreateHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = AFBookCreatePage(self)
        handler_page.render()
        return #0

class AFBookEditInfoHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = AFBookEditInfoPage(self)
        handler_page.render()
        return #0

class AFBookEditAboutHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = AFBookEditAboutPage(self)
        handler_page.render()
        return #0

class AFBookEditInviteHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = AFBookEditInvitePage(self)
        handler_page.render()
        return #0

class AFBookEditCatalogHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page =  AFBookEditCatalogPage(self)
        handler_page.render()
        return #0
