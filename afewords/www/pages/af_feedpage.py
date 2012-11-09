from basepage import *

@with_attr
class AFFeedPage(BasePage):
    __template_file__ = "afewords-feed/feed-index.html"

    ''' for url /feed '''
    doc = {
        'page_type': 'feed',
        'subpage_type': 'index',
        'feed_list': [],    # list, like blog list
    }


@with_attr
class AFFeedLikePage(BasePage):
    __template_file__ = "afewords-feed/feed-like.html"
    
    ''' for url /user-like '''
    doc = {
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
        'page_type': 'feed',
        'subpage_type': 'myself',
        'blog_list': [],
        'current_page': 1,
        'paging_html': '',
        'current_tag': 'default',
    }
