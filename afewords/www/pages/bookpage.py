#coding=utf-8

from basepage import BasePage, with_attr


@with_attr
class BookBasePage(BasePage):
    __template_file__ = 'book/book-base.html'
    doc = {
        'book':{},  # dict, see [[ book ]] in data_format
        'catalog_html': '', # unicode
        'load_page': 'cover',   # unicode, cover, summary, catalog, chapter
        'isedit' : False,
        'bid' : '', #id of book
    }

    def page_init(self):
        from toolpages import CatalogPage
        page = CatalogPage()
        page['isedit'] = self['isedit']
        page['node_list'] = self['book']['chapter_list']
        page['bid'] = self['bid']
        self['catalog_html'] = page.render_string()


@with_attr
class BookPage(BookBasePage): 
    __template_file__ = 'book/book-index.html'


@with_attr
class BookChapter(BookBasePage):
    __template_file__ = 'book/book-chapter.html'
    doc = {
        'load_page': 'chapter',
        'current_chapter': None,    # dict, see [[ chapter ]] in data_format 
    }

