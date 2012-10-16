#coding=utf-8

from basepage import BasePage, with_attr

@with_attr
class PagingPage(BasePage):
    '''
    create paging html
    '''
    __template_file__ = 'tool-paging.html'
    doc = {
        'current_page' : 1, # int , current_page
        'page_list' : [],   # list, [1,2,3,4,5]
        'base_url' : '',    # unicode, like /like?page=
    }


@with_attr
class CatalogPage(BasePage):
    '''
    create catalog block html
    '''
    __template_file__ = 'tool-catalog.html'
    doc = {
        'isedit': False,    # bollean
        'node_list': [],    # list
        'bid': '',  # unicode
    }
