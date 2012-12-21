#coding=utf-8
from basepage import with_attr, BaseRSSPage, BaseStringRender, BaseAtomPage

@with_attr
class ArticleFeedRender(BaseStringRender):
    __template_file__ = ''
    doc = {
        'article':{}
    }

@with_attr
class RSSRecentBlogPage(BaseRSSPage):
    doc = {
        'title' : u'子曰——最新博文',
        'link' : u'http://www.afewords.com/blog_recent',
        'description' : u'子曰最新的博文动态',
        'items' : [],
    }


@with_attr
class RSSUserBlogPage(BaseRSSPage):
    doc = {
        'title' : '',
        'link' : '',
        'description' : '',
        'items' : '',
    }

@with_attr
class AtomRecentBlogPage(BaseAtomPage):
    doc = {
        'title' : u'子曰——最新博文',
        'subtitle' : u'afewords',
        'feed_url' : u'http://www.afewords.com/blog_recent',
        'url' : u'http://www.afewords.com',
        'author' : u'Afewords',
        'entries' : [],
    }


@with_attr
class AtomUserBlogPage(BaseAtomPage):
    doc = {
    }
