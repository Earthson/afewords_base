# coding=utf-8
from basehandler import BaseHandler
from pages.pages import LoginPage
from generator import id_generator, index_generator


class LoginHandler(BaseHandler):
    def get(self):
        page = LoginPage(self)
        return page.render()
