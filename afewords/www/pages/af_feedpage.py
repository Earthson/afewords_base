#coding=utf-8
from basepage import *


@with_attr
class AFFeedPage(BasePage):
    __template_file__ = "afewords-feed/feed-index.html"

    ''' for url /feed '''
    doc = {
        'title': '动态 - 子曰',
        'page_type': 'feed',
        'subpage_type': 'feed',
        'feed_list': [],    # list, like blog list
        'id_list': [],
        'description': '动态聚合',
    }


@with_attr
class AFFeedLikePage(BasePage):
    __template_file__ = "afewords-feed/feed-like.html"
    
    ''' for url /user-like '''
    doc = {
        'title': '喜欢 - 子曰',
        'page_type': 'feed',
        'subpage_type': 'like',
        'like_list': [],    # list, like blog list
        'current_page': 1,
        'paging_html': '',  # for paging
        'page_all' : 1,
        'baseurl' : [],
        'urlparas' : {},
    }
    def page_init(self):
        from toolpages import PagingPage
        tmp = PagingPage()
        tmp['current_page'] = self['current_page']
        tmp.set_by(self['baseurl'], self['urlparas'], self['page_all'])
        self['paging_html'] = tmp.render_string()


@with_attr
class AFFeedMyselfPage(BasePage):
    ''' for url /blog-lib '''
    __template_file__ = "afewords-feed/feed-myself.html"
    doc = {
        'title': '我的文章 - 子曰',
        'page_type': 'feed',
        'subpage_type': 'myself',
        'tag_list' : [],
        'blog_list': [],
        'current_page': 1,
        'paging_html': '',
        'current_tag': 'default',
        'page_all' : 1,
        'baseurl' : [],
        'urlparas' : {},
    }

    def page_init(self):
        from toolpages import PagingPage
        tmp = PagingPage()
        tmp['current_page'] = self['current_page']
        tmp.set_by(self['baseurl'], self['urlparas'], self['page_all'])
        self['paging_html'] = tmp.render_string()

@with_attr
class AFFeedbackPage(BasePage):
    ''' for url /afewords-feedback '''
    __template_file__ = "afewords-feed/feed-feedback.html"
    doc = {
        'title': '反馈 - 子曰',
        'feedback_list': [],
        'subpage_type': 'feedback',
        'current_page': 1,
        'paging_html': '',
    }
