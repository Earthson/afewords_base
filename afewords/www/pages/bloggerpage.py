#coding=utf-8

from basepage import BasePage, with_attr


@with_attr
class BloggerPage(BasePage):
    __template_file__ = 'blogger/blogger-base.html'
    doc = {
        'blogger_type' : 'blog',
        'author' : {},  # see [[ author ]] in data_format
        'current_page' : 1, # int 
        'paging_html' : '', # unicode, for paging
        'tag_list' : [],    # see [[tag_list]]
        'current_tag' : 'default', # unicode
        'page_list' : [],
        'baseurl' : [],
        'urlparas' : {},
    }

    def page_init(self):
        from toolpages import PagingPage
        tmp = PagingPage()
        tmp.set_by(self['baseurl'], self['urlparas'], self['page_list'])
        self['paging_html'] = tmp.render_string()


@with_attr
class BloggerBlogPage(BloggerPage):
    __template_file__ = 'blogger/blogger-index.html'
    doc = {
        'blogger_type' : 'blog',
        'blog_list' : [],   # see [[ blog_list ]] in data_format
    } 


@with_attr
class BloggerLikePage(BloggerPage):
    __template_file__ = 'blogger/blogger-like.html'
    doc = {
        'blogger_type' : 'like',
        'like_list' : [],   # see [[ like_list ]] in data_format
    }


@with_attr
class BloggerBookPage(BloggerPage):
    __template_file__ = 'blogger/blogger-book.html'
    doc = {
        'blogger_type' : 'book',
        'book_list' : [],   # see [[ book_list ]] in data_format
    }


@with_attr
class BloggerFollowPage(BloggerPage):
    __template_file__ = 'blogger/blogger-follow.html'
    doc = {
        'blogger_type' : 'follow',
        'follow_list' : [], # see [[ follow_list ]] in data_format
    }

@with_attr
class BloggerAboutPage(BloggerPage):
    __template_file__ = 'blogger/blogger-about.html'
    doc = {
        'blogger_type' : 'about',
        'about' : {},   # see [[ article ]] in data_format
    }
