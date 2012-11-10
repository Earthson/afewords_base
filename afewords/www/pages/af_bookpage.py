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
        'title': '创建知识谱 - 子曰',
        'page_type': 'book',
        'subpage_type': 'create',
    }


@with_attr
class AFBookEditBasePage( BasePage ):
    __template_file__ = "afewords-book/book-edit-base.html"
    doc = {
        'title': '修改知识谱 - 子曰',
        'page_type': 'book',
        'subpage_type': 'myself',
        'edit_type': 'index',
        'book': [], 
    }

@with_attr
class AFBookEditInfoPage( AFBookEditBasePage):
    ''' for url /book-edit '''
    __template_file__ = "afewords-book/book-edit-info.html"
    doc = {
        'edit_type': 'info',
    }

@with_attr
class AFBookEditCatalogPage( AFBookEditBasePage ):
    ''' for url /book-eidt?id=xxx&type=catalog '''
    __template_file__ = "afewords-book/book-edit-catalog.html"
    doc = {
        'edit_type': 'catalog',
    }

@with_attr
class AFBookEditInvitePage( AFBookEditBasePage ):
    ''' for url /book-edit?id=xxx&type=invite '''
    __template_file__ = "afewords-book/book-edit-invite.html"
    doc = {
        'edit_type': 'invite',
    }

@with_attr
class AFBookEditAboutPage( AFBookEditBasePage ):
    ''' for url /book-edit?id=xxxx&type=about '''
    __template_file__ = "afewords-book/book-edit-about.html"
    doc = {
        'edit_type': 'invite',
        'about': {},    # dict, article src
    }
