#coding=utf-8
from basepage import *

@with_attr
class AFBookPage(BasePage):
    __template_file__ = "afewords-book/book-index.html"
    ''' for url /afewords-book '''
    doc = {
        'title': '知识谱 - 子曰',
        'page_type': 'book',
        'subpage_type': 'index',
        'current_page' : 1,
        'paging_html': '',  # for paging
        'book_list': None,  # list
    }

@with_attr
class AFBookMyselfPage(BasePage):
    __template_file__ = "afewords-book/book-myself.html"
    ''' for url /user-book '''
    doc = {
        'title': '我的知识谱 - 子曰',
        'page_type': 'book',
        'subpage_type': 'myself',
        'current_page': 1,
        'paging_html': '',  # for paging
        'book_list': None,  # list
    }


@with_attr
class AFBookCreatePage( BasePage ):
    __template_file__ = "afewords-book/book-create.html"
    ''' for url /book-create '''
    doc = {
        'title': '创建知识谱 - 子曰'
        'page_type': 'book',
        'subpage_type': 'create',
    }
