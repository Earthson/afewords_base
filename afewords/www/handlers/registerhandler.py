# coding=utf-8
from basehandler import *
from pages.pages import RegisterPage
from generator import id_generator, index_generator


class RegisterHandler(BaseHandler):

    @with_nologin
    def get(self):
        page = RegisterPage(self)
        return page.render()

    @with_nologin
    def post(self):
        pass
