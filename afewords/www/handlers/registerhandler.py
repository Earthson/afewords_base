# coding=utf-8
from basehandler import BaseHandler
from pages.pages import RegisterPage
from generator import id_generator, index_generator


class RegisterHandler(BaseHandler):
    def get(self):
        page = RegisterPage(self)
        return page.render()
