#coding=utf-8

from basepage import BasePage, with_attr


@with_attr
class BookBasePage(BasePage):
    __template_file__ = 'book-base.html'
    doc = {
        'book':{},  # dict, see [[ book ]] in data_format
        'catalog_html': '', # unicode
        'want_page': 'cover',   # unicode, cover, summary, catalog, chapter
    }


@with_attr
class BookPage(BookBasePage): 
    __template_file__ = 'book-index.html'
    doc = {
        'isedit': False,    # bollean
    }

@with_attr
class BookChapter(BookBasePage):
    __template_file__ = 'book-chapter.html'
    doc = {
        'current_chapter': dict,    # see [[ chapter ]] in data_format 
    }
