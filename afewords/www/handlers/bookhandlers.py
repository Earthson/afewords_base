#coding=utf-8

from basehandler import *
from pages.bookpage import BookPage, BookChapter


class BookHandlerPara(BaseHandlerPara):

    paradoc = {
        #todo deju
    }


class BookHandler(BaseHandler):
    def get(self):
        handelr_paras = BookHandlerPara(self)
        handler_page = BookPage
        usr = self.current_user
        #todo Earthson
        handler.by_status(0)
        handler.render()
        return
