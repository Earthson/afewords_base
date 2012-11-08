#coding=utf-8
from basepage import *

from toolpages import PagingPage

@with_attr
class AFUserLibPage(BasePage):
    ''' for url /user-lib '''
    __template_file__ = "afewords-user/user-index.html"
    doc = {
        'page_type': 'user',
        'subpage_type': 'index',
        'title': '人群 - 子曰',
        'user_list': [],    # list 
        'current_page': 1,
        'paging_html': '',
    }
