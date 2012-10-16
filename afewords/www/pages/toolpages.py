#coding=utf-8

from basepage import BaseToolPage, with_attr

@with_attr
class PagingPage(BaseToolPage):
    '''
    create paging html
    '''
    __template_file__ = 'tool-paging.html'
    doc = {
        'current_page' : 1, # int , current_page
        'page_list' : [],   # list, [1,2,3,4,5]
        'urls' : [],    # unicode, like /like?page=
    }
    
    def get_urls(self, base_url='', para_dic=None, page_list):
        from afutils.url_utils import url_with_para
        self['page_list'] = [each for each in page_list]
        para_dic = dict() if para_dic is None else dict(para_dic)
        para_dics = [dict(para_dic.items()+('page', each)) 
                        for each in self['page_list']]
        self['urls'] = [url_with_para(base_url, each) for each in para_dics]


@with_attr
class CatalogPage(BaseToolPage):
    '''
    create catalog block html
    '''
    __template_file__ = 'tool-catalog.html'
    doc = {
        'isedit': False,    # bollean
        'node_list': [],    # list
        'bid': '',  # unicode
    }
