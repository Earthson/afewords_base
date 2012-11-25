# coding=utf-8
from afutils.security import *
from basehandler import *
from pages.pages import *
from generator import id_generator, index_generator

from pages.errorpage import BaseErrorPage
class AFNotFoundHandler(BaseHandler):

    def get(self):
        errorpage = BaseErrorPage(self)
        errorpage['status'] = 404
        return errorpage.render()

