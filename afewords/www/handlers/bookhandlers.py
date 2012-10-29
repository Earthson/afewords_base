#coding=utf-8

from basehandler import *
from pages.bookpage import BookPage, BookChapter


class BookHandlerPara(BaseHandlerPara):

    paradoc = {
        #todo deju
        'edit': 'yes',  # unicode, yes or not, edit book or not
        'load': 'cover',    # unicode, cover or summary or catalog
    }

    def read(self):
        BaseHandlerPara.read(self)
        if self['load'] not in ('cover', 'summary', 'catalog', 'chapter'):
            self['load'] = 'cover'
        self['edit'] = False if self['edit'] == 'not' else True


class BookHandler(BaseHandler):
    '''
        bid get from url
    '''
    def get(self, bid):
        from article.catalog import Catalog
        handler_paras = BookHandlerPara(self)
        handler_page = BookPage(self)
        usr = self.current_user
        handler_page['edit'] = handler_paras['edit']
        handler_page['load_page'] = handler_paras['load']
        catalog_obj = Catalog.by_id(bid)
        if catalog_obj is None:
            self.send_error(404)
            return
        handler_page['book'] = catalog_obj.basic_info
        handler_page.render()
        return
