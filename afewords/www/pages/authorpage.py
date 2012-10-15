#coding=utf-8

from basepage import BasePage, with_attr


@with_attr
class AuthorPage(BasePage):
    __template_file__ = 'bloger-base.html'
    doc = {
        'bloger_type' : 'blog',
        'author' : {},  # see [[ author ]] in data_format
        'current_page' : 1, # int 
        'paging_html' : '', # unicode, for paging
        'tag_list' : [],    # see [[tag_list]]
        'current_tag' : 'default' # unicode
    }


@with_attr
class AuthorBlogPage(AuthorPage):
    __template_file__ = 'bloger-index.html'
    doc = {
        'bloger_type' : 'blog',
        'blog_list' : [],   # see [[ blog_list ]] in data_format
    } 


@with_attr
class AuthorLikePage(AuthorPage):
    __template_file__ = 'bloger-like.html'
    doc = {
        'bloger_type' : 'like',
        'like_list' : [],   # see [[ like_list ]] in data_format
    }


@with_attr
class AuthorBookPage(AuthorPage):
    __template_file__ = 'bloger-book.html'
    doc = {
        'bloger_type' : 'book',
        'book_list' : [],   # see [[ book_list ]] in data_format
    }


@with_attr
class AuthorFollowPage(AuthorPage):
    __template_file__ = 'bloger-follow.html'
    doc = {
        'bloger_type' : 'follow',
        'follow_list' : [], # see [[ follow_list ]] in data_format
    }

@with_attr
class AuthorAboutPage(AuthorPage):
    __template_file__ = 'bloger-about.html'
    doc = {
        'bloger_type' : 'about',
        'about' : {},   # see [[ article ]] in data_format
    }
