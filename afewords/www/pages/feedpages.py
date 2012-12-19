#coding=utf-8
from basepage import with_attr, BaseFeedPage

@with_attr
class RSSRecentBlogPage(BaseFeedPage):
    doc = {
        'title' : u'子曰——最新博文',
        'link' : u'http://www.afewords.com/blog_recent',
        'description' : u'子曰最新的博文动态',
        'items' : [],
    }


@with_attr
class RSSUserBlogPage(BaseFeedPage):
    doc = {
        'title' : '',
        'link' : '',
        'description' : '',
        'items' : '',
    }
