# coding=utf-8
from afutils.security import *
from basehandler import *
from pages.pages import IndexPage

class IndexHandler(BaseHandler):

    def get(self):
        self.redirect('/login')
        return
        page = IndexPage(self)
        return page.render()
