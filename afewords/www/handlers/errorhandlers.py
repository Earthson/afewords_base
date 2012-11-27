# coding=utf-8
from basehandler import *

class AFNotFoundHandler(BaseHandler):

    def get(self, tovisit):
        from pages.errorpage import BaseErrorPage
        errorpage = BaseErrorPage(self)
        errorpage['status'] = 404
        errorpage['error_info'] = 'UnknowURL:' + tovisit
        return errorpage.render()
