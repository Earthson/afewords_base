#coding=utf-8

from basepage import BasePage, with_attr


@with_attr
class AuthorPage(BasePage):
    __template_file__ = 'bloger.html'
    doc = {
        'bloger_type' : 'blog',
        'author' : {},  # see [[ author ]] in data_format
    }


@with_attr
class AuthorBlogPage(AuthorPage):
    doc = {
        'bloger_type' : 'blog',
        'blog_list' : [],   # see [[ blog_list ]] in data_format
    } 


@with_attr
class AuthorLikePage(AuthorPage):
    doc = {
        'bloger_type' : 'like',
        'like_list' : [],   # see [[ like_list ]] in data_format
    }


@with_attr
class AuthorBookPage(AuthorPage):
    doc = {
        'bloger_type' : 'book',
        'book_list' : [],   # see [[ book_list ]] in data_format
    }


@with_attr
class AuthorFollowPage(AuthorPage):
    doc = {
        'bloger_type' : 'follow',
        'follow_list' : [], # see [[ follow_list ]] in data_format
    }

@with_attr
class AuthorAboutPage(AuthorPage):
    doc = {
        'bloger_type' : 'about',
        'about' : {},   # see [[ article ]] in data_format
    }
