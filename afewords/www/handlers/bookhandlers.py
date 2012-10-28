#coding=utf-8

from basehandler import *
from pages.bookpage import BookPage, BookChapter


class BookHandlerPara(BaseHandlerPara):

    paradoc = {
        #todo deju
        'load': 'cover',    # unicode, cover or summary or catalog
    }

    def read(self):
        BaseHandlerPara.read(self)
        if self['load'] not in ('cover', 'summary', 'catalog', 'chapter'):
            self['load'] = 'cover'


class BookHandler(BaseHandler):
    def get(self, bid):
        from article.catalog import Catalog
        handelr_paras = BookHandlerPara(self)
        handler_page = BookPage(self)
        usr = self.current_user
        catalog_obj = Catalog.by_id(bid)
        if catalog_obj is None:
            self.send_error(404)
            return
        handler['book'] = catalog_obj.basic_info
        handler.by_status(0)
        handler.render()
        return
