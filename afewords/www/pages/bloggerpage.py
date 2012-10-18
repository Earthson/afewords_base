#coding=utf-8

from basepage import BasePage, with_attr


@with_attr
class BloggerPage(BasePage):
    __template_file__ = 'blogger-base.html'
    doc = {
        'blogger_type' : 'blog',
        'author' : {},  # see [[ author ]] in data_format
        'current_page' : 1, # int 
        'paging_html' : '', # unicode, for paging
        'tag_list' : [],    # see [[tag_list]]
        'current_tag' : 'default' # unicode
    }



@with_attr
class BloggerBlogPage(AuthorPage):
    __template_file__ = 'blogger-index.html'
    doc = {
        'blogger_type' : 'blog',
        'blog_list' : [],   # see [[ blog_list ]] in data_format
    } 


@with_attr
class BloggerLikePage(AuthorPage):
    __template_file__ = 'blogger-like.html'
    doc = {
        'blogger_type' : 'like',
        'like_list' : [],   # see [[ like_list ]] in data_format
    }


@with_attr
class BloggerBookPage(AuthorPage):
    __template_file__ = 'blogger-book.html'
    doc = {
        'blogger_type' : 'book',
        'book_list' : [],   # see [[ book_list ]] in data_format
    }


@with_attr
class BloggerFollowPage(AuthorPage):
    __template_file__ = 'blogger-follow.html'
    doc = {
        'blogger_type' : 'follow',
        'follow_list' : [], # see [[ follow_list ]] in data_format
    }

@with_attr
class BloggerAboutPage(AuthorPage):
    __template_file__ = 'blogger-about.html'
    doc = {
        'blogger_type' : 'about',
        'about' : {},   # see [[ article ]] in data_format
    }
