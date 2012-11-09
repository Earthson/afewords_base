#coding=utf-8

import re
from basehandler import *

from article.catalog import Catalog
from user import User

from authority import *

class CatalogSectionModifyPara(BaseHandlerPara):
    paradoc = {
        'book_id' : '',
        'node_id' : '',
        'section' : '',
        'title' : '',
    }

from pages.postjson import CatalogSectionModifyJson

class CatalogSectionModifyHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = CatalogSectionModifyPara(self)
        handler_json = CatalogSectionModifyJson(self)
        usr = self.current_user
        book = Catalog.by_id(handler_para['book_id'])
        if book is None:
            handler_json.by_status(3)
            handler_json.write()
            return #book not exist
        auth_tmp = book.authority_verify(usr=usr, env=book)
        if test_auth(auth_tmp, A_WRITE) is False:
            handler_json.by_status(5)
            handler_json.write()
            return #permission denied
        if not handler_para['section']:
            handler_json.by_status(1)
            handler_json.write()
            return #section is empty
        if not handler_para['title']:
            handler_json.by_status(2)
            handler_json.write()
            return #title is empty
        if not book.modify_node(handler_para['node_id'], 
                    handler_para['title'], handler_para['section']):
            handler_json.by_status(4)
            handler_json.write()
            return #node not exist
        handler_json.by_status(0)
        handler_json.write()
        return #0 


class CatalogSectionNewPara(BaseHandlerPara):
    paradoc = {
        'book_id' : '',
        'section' : '',
        'title' : '',
    }

from pages.postjson import CatalogSectionNewJson

class CatalogSectionNewHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = CatalogSectionNewPara(self)
        handler_json = CatalogSectionNewJson(self)
        usr = self.current_user
        book = Catalog.by_id(handler_para['book_id'])
        if book is None:
            handler_json.by_status(3)
            handler_json.write()
            return #book not exist
        auth_tmp = book.authority_verify(usr=usr, env=book)
        if test_auth(auth_tmp, A_WRITE) is False:
            handler_json.by_status(5)
            handler_json.write()
            return #permission denied
        if not handler_para['section']:
            handler_json.by_status(1)
            handler_json.write()
            return #section is empty
        if not handler_para['title']:
            handler_json.by_status(2)
            handler_json.write()
            return #title is empty
        handler_json['node_id'] = book.add_node(handler_para['title'], 
                                                handler_para['section'])
        handler_json.by_status(0)
        handler_json.write()
        return #0


class CatalogSectionDelPara(BaseHandlerPara):
    paradoc = {
        'book_id' : '',
        'node_id' : '',
    }

from pages.postjson import CatalogSectionDelJson

class CatalogSectionDelHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = CatalogSectionDelPara(self)
        handler_para = CatalogSectionDelJson(self)
        usr = self.current_user
        book = Catalog.by_id(handler_para['book_id'])
        if book is None:
            handler_json.by_status(1)
            handler_json.write()
            return #book not exist
        auth_tmp = bookauthority_verify(usr=usr, env=book)
        if test_auth(auth_tmp, A_DEL) is False:
            handler_json.by_status(5)
            handler_json.write()
            return #permission dined
        if not handler_para['node_id'] or \
                book.remove_node(handler_para['node_id']) is False:
            handler_json.by_status(2)
            handler_json.write()
            return #node not exist
        handler_json.by_status(0)
        handler_json.write()
        return #0