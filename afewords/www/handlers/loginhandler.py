# coding=utf-8
from basehandler import BaseHandler

from generator import id_generator, index_generator


class LoginHandler(BaseHandler):
    def get(self):
        return self.write('Hello world!')
