#coding=utf-8
from basepage import *


@with_attr
class AFFeedPage(BasePage):
    __template_file__ = "afewords-feed/feed-index.html"

    ''' for url /feed '''
    doc = {
        'title': '动态 - 子曰',
        'page_type': 'feed',
        'subpage_type': 'index',
        'feed_list': [],    # list, like blog list
    }


@with_attr
class AFFeedLikePage(BasePage):
    __template_file__ = "afewords-feed/feed-like.html"
    
    ''' for url /user-like '''
    doc = {
        'title': '收藏 - 子曰',
        'page_type': 'feed',
        'subpage_type': 'like',
        'like_list': [],    # list, like blog list
        'current_page': 1,
        'paging_html': '',  # for paging
    }

@with_attr
class AFFeedMyselfPage(BasePage):
    ''' for url /blog-lib '''
    __template_file__ = "afewords-feed/feed-myself.html"
    doc = {
        'title': '我的动态 - 子曰',
        'page_type': 'feed',
        'subpage_type': 'myself',
        'blog_list': [],
        'current_page': 1,
        'paging_html': '',
        'current_tag': 'default',
        'page_list' : [],
        'baseurl' : [],
        'urlparas' : {},
    }

    def page_init(self):
        from toolpages import PagingPage
        if len(self['page_list']) <= 1:
            self['page_list'] = []
        tmp = PagingPage()
        tmp['current_page'] = self['current_page']
        tmp.set_by(self['baseurl'], self['urlparas'], self['page_list'])
        self['paging_html'] = tmp.render_string()

