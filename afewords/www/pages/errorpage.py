#coding=utf-8
from basepage import BasePage, with_attr


@with_attr
class BaseErrorPage(BasePage):
    __template_file__ = 'afewords-error.html'

    doc = {
        'status' : 500,
        'error_info' : '',
    }
