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
        'page_all' : 1,
        'urls' : [],    # unicode, like /like?page=
        'page_list' : [], # list of page_number
        'first' : None,
        'last' : None,
    }

    def set_page_list(self, expand=2):
        cc = self['current_page']
        if self['page_all'] <= 1:
            return
        st = cc - 2 if cc > 2 else 1
        ed = cc + 2 if cc + 2 <= self['page_all'] else self['page_all']
        self['page_list'] = range(st, ed+1)
        if st > 1:
            self['first'] = 1
        if ed < self['page_all']:
            self['last'] = self['page_all']
    
    def set_by(self, baseurl='', paradoc=None, page_all=1):
        from afutils.url_utils import url_with_para
        self['page_all'] = page_all
        self.set_page_list(expand=2)
        paradoc = dict() if paradoc is None else dict(paradoc)
        paradocs = [dict(paradoc, page=each) 
                        for each in self['page_list']]
        self['urls'] = [url_with_para(baseurl, each) for each in paradocs]
        if self['first'] is not None:
            self['first'] = url_with_para(baseurl, 
                    dict(paradoc, page=self['first']))
        if self['last'] is not None:
            self['last'] = url_with_para(baseurl, 
                    dict(paradoc, page=self['last']))


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

@with_attr
class WriteTitlePage(BaseToolPage):
    ''' 
    title in write page
    '''
    __template_file__ = 'tool-writetitle.html'
    article_type_dict = {
        'blog': "文章",
        'user-about': "关于",
        'book-about': " 知识谱摘要",
        'group-about': "关于",
        'group-feedback': "反馈",
        'group-doc': "文档",
        'group-bulletin': "公告",
        'group-topic': "话题",
    }
    doc = {
        'isedit': False,
        'env': {},    # dict
        'article_type': 'blog', # unicode
        'article_type_dict': article_type_dict,
    }
