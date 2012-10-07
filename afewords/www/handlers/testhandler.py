# coding=utf-8
from afutils.security import *
from basehandler import *
from pages.pages import *
from generator import id_generator, index_generator

from afutils.security import *

class TestHandler(BaseHandler):

    def get(self):
        page = TestPage(self)
        return page.render()

