# coding=utf-8

from afutils.security import *
from basehandler import *
from pages.authorpage import AuthorBlogPage

class UserBlogLibHandler(BaseHandler):
    def get(self):
        page = AuthorBlogPage(self)
        pass
