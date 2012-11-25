#coding=utf-8

from basehandler import *
from pages.af_bookpage import *

from article.catalog import Catalog
from global_info import recent_books

from authority import *

class AFBookHandler(BaseHandler):
    def get(self):
        handler_page = AFBookPage(self)
        usr = self.current_user
        try:
            books = sorted(Catalog.by_ids(recent_books.get_slice(-20)), 
                                reverse=False)
        except:
            books = []
        handler_page['book_list'] = [each.obj_info_view_by('overview_info',
                usr=usr, env=None) for each in books]
        handler_page.render()
        return #0


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


class AFBookCreatePara(BaseHandlerPara):
    paradoc = {
        'name' : '',
        'keywords' : '',
    }

    def read(self):
        BaseHandlerPara.read(self)
        self['keywords'] = self['keywords'].replace(u'，', u',')
        self['keywords'] = self['keywords'].split(',')

from pages.postjson import AFBookCreateJson

class AFBookCreateHandler(BaseHandler):
    @with_login
    def get(self):
        handler_page = AFBookCreatePage(self)
        handler_page.render()
        return #0

    @with_login_post
    def post(self):
        handler_para = AFBookCreatePara(self)
        handler_json = AFBookCreateJson(self)
        if not handler_para['name']:
            handler_json.by_status(1)
            handler_json.write()
            return #name is empty
        usr = self.current_user
        book_new = usr.create_catalog(handler_para['name'], 
                                        handler_para['keywords'])
        handler_json['about_id'] = str(book_new.about_id)
        recent_books.pop_head()
        recent_books.push(book_new._id)
        handler_json.by_status(0)
        handler_json.write()
        return

def bookedit_init(handler, bid, page):
    book = Catalog.by_id(bid)
    if book is None:
        return 1 #book not exist
    usr = handler.current_user
    auth_tmp = book.authority_verify(usr=usr, env=book)
    if test_auth(auth_tmp, A_WRITE) is False:
        return 2 #permission denied
    handler.book = book
    

class AFBookEditInfoHandler(BaseHandler):
    @with_login
    def get(self, bid):
        handler_page = AFBookEditInfoPage(self)
        status = bookedit_init(self, bid, handler_page)
        usr = self.current_user
        if status == 1:
            self.send_error(404)
            return #book not found
        if status == 2:
            self.handler_page.render()
            return #permission denied
        handler_page['book'] = self.book.obj_info_view_by('edit_info',
                                usr=usr, env=self.book)
        handler_page.render()
        return #0

class AFBookEditAboutHandler(BaseHandler):
    @with_login
    def get(self, bid):
        handler_page = AFBookEditAboutPage(self)
        status = bookedit_init(self, bid, handler_page)
        usr = self.current_user
        if status == 1:
            self.send_error(404)
            return #book not found
        if status == 2:
            self.handler_page.render()
            return #permission denied
        handler_page['book'] = self.book.obj_info_view_by('edit_with_summary',
                                usr=usr, env=self.book)
        handler_page.render()
        return #0

class AFBookEditInviteHandler(BaseHandler):
    @with_login
    def get(self, bid):
        handler_page = AFBookEditInvitePage(self)
        status = bookedit_init(self, bid, handler_page)
        usr = self.current_user
        if status == 1:
            self.send_error(404)
            return #book not found
        if status == 2:
            self.handler_page.render()
            return #permission denied
        handler_page['book'] = self.book.obj_info_view_by('basic_info',
                                usr=usr, env=self.book)
        handler_page.render()
        return #0

class AFBookEditCatalogHandler(BaseHandler):
    @with_login
    def get(self, bid):
        handler_page =  AFBookEditCatalogPage(self)
        status = bookedit_init(self, bid, handler_page)
        usr = self.current_user
        if status == 1:
            self.send_error(404)
            return #book not found
        if status == 2:
            #handler_page.render()
            self.redirect('/')
            return #permission denied
        handler_page['bid'] = bid
        handler_page['book'] = self.book.obj_info_view_by('basic_info',
                                usr=usr, env=self.book)
        handler_page.page_init()
        handler_page.render()
        return #0
