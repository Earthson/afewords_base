#coding=utf-8

from basepage import BasePage, with_attr


@with_attr
class BookPage(BasePage):
    __template_file__ = 'book-base.html'
    doc = {}


