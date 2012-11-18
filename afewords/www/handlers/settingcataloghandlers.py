#coding=utf-8

import re
from basehandler import *

from article.catalog import Catalog
from user import User
from generator import generator

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
        handler_json = CatalogSectionDelJson(self)
        usr = self.current_user
        book = Catalog.by_id(handler_para['book_id'])
        if book is None:
            handler_json.by_status(1)
            handler_json.write()
            return #book not exist
        auth_tmp = book.authority_verify(usr=usr, env=book)
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


class RecArticleToBookPara(BaseHandlerPara):
    paradoc = {
        'book_id' : '',
        'node_id' : '',
        'article_id' : '',
        'article_type' : 'blog',
    }


from pages.postjson import RecArticleToBookJson

class RecArticleToBookHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = RecArticleToBookPara(self)
        handler_json = RecArticleToBookJson(self)
        usr = self.current_user
        book = Catalog.by_id(handler_para['book_id'])
        if book is None:
            handler_json.by_status(2)
            handler_json.write()
            return #book not exist
        article_obj = generator(handler_para['article_id'], 
                                handler_para['article_type'])
        if article_obj is None:
            handler_json.by_status(1)
            handler_json.write()
            return #article not exist
        rr = article_obj.add_to_catalog(book, handler_para['node_id'])
        if rr is None:
            handler_json.by_status(3)
            handler_json.write()
            return #section not exist
        handler_json['book_title'] = book.name
        handler_json['chapter_title'] = book.get_node_dict(node_id)['title']
        handler_json['article_title'] = article_obj.name
        handler_json['relation_id'] = rr.uid
        handler_json.by_status(0)
        handler_json.write()
        return #0

class DelArticleFromBookPara(BaseHandlerPara):
    paradoc = {
        'book_id' : '',
        'node_id' : '',
        'article_id' : '',
        'article_type' : 'blog',
    }


from pages.postjson import DelArticleFromBookJson

class DelArticleFromBookHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = DelArticleFromBookPara(self)
        handler_json = DelArticleFromBookJson(self)
        usr = self.current_user
        book = Catalog.by_id(handler_para['book_id'])
        article_obj = generator(handler_para['article_id'], 
                                handler_para['article_type'])
        if article_obj is None:
            handler_json.by_status(1)
            handler_json.write()
            return #article not exist
        auth_tmp = article_obj.authority_verify(usr, env=book)
        if book is not None:
            auth_tmp |= book.authority_verify(usr, env=book)
        if test_auth(auth_tmp, A_WRITE) is False:
            handler_json.by_status(2)
            handler_json.write()
            return #permission denied
        rr = article_obj.remove_from_catalog(book, handler_para['node_id'])
        handler_json.by_status(0)
        handler_json.write()
        return #0

from relation import Relation

class SpecArticleToBookPara(BaseHandlerPara):
    paradoc = {
        'book_id' : '',
        'node_id' : '',
        'relation_id' : '',
    }

from pages.postjson import SpecArticleToBookJson

class SpecArticleToBookHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = SpecArticleToBookPara(self)
        handler_json = SpecArticleToBookJson(self)
        usr = self.current_user
        book = Catalog.by_id(handler_para['book_id'])
        relation_obj = Relation.by_id(handler_para['relation_id'])
        if book is None:
            handler_json.by_status(2)
            handler_json.write()
            return #book not exist
        if relation_obj is None:
            handler_json.by_status(1)
            handler_json.write()
            return #relation not exist
        auth_tmp = book.authority_verify(usr, env=book)
        if test_auth(auth_tmp, A_WRITE) is False:
            handler_json.by_status(4)
            handler_json.write()
            return #permission denied
        status = book.spec_article_to(handler_para['node_id'], relation_obj)
        if status is False:
            handler_json.by_status(3)
            handler_json.write()
            return #set failed, node_id may not exist
        handler_json.by_status(0)
        handler_json.write()
        return #0

class UnSpecArticleFromBookPara(BaseHandlerPara):
    paradoc = {
        'book_id' : '',
        'node_id' : '',
        'relation_id' : '',
    }

from pages.postjson import UnSpecArticleFromBookJson

class UnSpecArticleFromBookHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_para = UnSpecArticleFromBookPara(self)
        handler_json = UnSpecArticleFromBookJson(self)
        usr = self.current_user
        book = Catalog.by_id(handler_para['book_id'])
        relation_obj = Relation.by_id(handler_para['relation_id'])
        if book is None:
            handler_json.by_status(2)
            handler_json.write()
            return #book not exist
        if relation_obj is None:
            handler_json.by_status(1)
            handler_json.write()
            return #relation not exist
        auth_tmp = book.authority_verify(usr, env=book)
        if test_auth(auth_tmp, A_WRITE) is False:
            handler_json.by_status(4)
            handler_json.write()
            return #permission denied
        status = book.unspec_article_to(handler_para['node_id'], relation_obj)
        if status is False:
            handler_json.by_status(3)
            handler_json.write()
            return #set failed, node_id may not exist
        handler_json.by_status(0)
        handler_json.write()
        return #0
