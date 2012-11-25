#coding=utf-8

from basehandler import *
from pages.bookpage import BookPage, BookChapterPage, BookAboutPage, BookCatalogPage, BookInfoPage



class BookHandler(BaseHandler):
    '''
        bid get from url
    '''
    def get(self, bid):
        from article.catalog import Catalog
        handler_page = BookPage(self)
        usr = self.current_user
        handler_page['bid'] = bid
        catalog_obj = Catalog.by_id(bid)
        if catalog_obj is None:
            self.send_error(404)
            return
        handler_page['book'] = catalog_obj.obj_info_view_by('basic_info', 
                                    usr=usr)
        handler_page.page_init()
        
        book_name = handler_page['book']['name']
        handler_page['title'] = book_name + u' - 子曰知识谱'
        handler_page['meta_keywords'] = handler_page['book']['keywords']
        handler_page['description'] = u'知识谱' + book_name

        handler_page.render()
        return


class BookAboutHandler(BaseHandler):
    '''
        bid get from url
    '''
    def get(self, bid):
        from article.catalog import Catalog
        handler_page = BookAboutPage(self)
        usr = self.current_user
        handler_page['bid'] = bid
        catalog_obj = Catalog.by_id(bid)
        if catalog_obj is None:
            self.send_error(404)
            return
        handler_page['book'] = catalog_obj.obj_info_view_by('with_summary', 
                                    usr=usr)
        handler_page.page_init()

        book_name = handler_page['book']['name']
        handler_page['title'] = book_name + u' -  摘要 - 子曰知识谱'
        handler_page['meta_keywords'] = handler_page['book']['keywords']
        handler_page['description'] = u'知识谱' + book_name + u'摘要'

        handler_page.render()
        return

class BookCatalogHandler(BaseHandler):
    '''
        url /book/xxx/catalog
        bid get from url
    '''
    def get(self, bid):
        from article.catalog import Catalog
        handler_page = BookCatalogPage(self)
        usr = self.current_user
        handler_page['bid'] = bid
        catalog_obj = Catalog.by_id(bid)
        if catalog_obj is None:
            self.send_error(404)
            return
        handler_page['book'] = catalog_obj.obj_info_view_by('basic_info', 
                                    usr=usr)
        handler_page.page_init()
        book_name = handler_page['book']['name']
        handler_page['title'] = book_name + u' - 子曰知识谱'
        handler_page['meta_keywords'] = handler_page['book']['keywords']
        handler_page['description'] = u'知识谱' + book_name + u'目录'
        handler_page.render()
        return


class BookChapterHandler(BaseHandler):
    def get(self, bid, cnum):
        from article.catalog import Catalog
        handler_page = BookChapterPage(self)
        usr = self.current_user
        catalog_obj = Catalog.by_id(bid)
        if catalog_obj is None:
            self.send_error(404)
            return
        chapter_info = catalog_obj.get_node_info_view_by(cnum, usr, catalog_obj)
        if chapter_info is None:
            self.send_error(404)
            return
        handler_page['current_chapter'] = chapter_info
        handler_page['book'] = catalog_obj.obj_info_view_by('basic_info', 
                                    usr, catalog_obj)
        cids = [each['cid'] for each in handler_page['book']['chapter_list']]
        cid = chapter_info['cid']
        pre, nxt = None, None
        for i in xrange(len(cids)): #get position of current
            if cid == cids[i]:
                pre = i - 1 if i > 0 else None
                nxt = i + 1 if i + 1 < len(cids) else None
                break
        handler_page['previous_chapter'] = None if pre is None else \
                handler_page['book']['chapter_list'][pre] 
        handler_page['next_chapter'] = None if nxt is None else \
                handler_page['book']['chapter_list'][nxt]
        handler_page['bid'] = bid
        handler_page.page_init()

        book_name = handler_page['book']['name']
        chapter_num = handler_page['current_chapter']['chapter_num']
        chapter_name = handler_page['current_chapter']['title']
        handler_page['title'] = chapter_num + u' -  ' +chapter_name + u' - ' + book_name
        handler_page['meta_keywords'] = handler_page['book']['keywords']
        handler_page['description'] = book_name + u',' + chapter_name
        handler_page.render()
        return


class BookInfoHandler(BaseHandler):
    '''
        bid get from url
    '''
    def get(self, bid):
        from article.catalog import Catalog
        handler_page = BookInfoPage(self)
        usr = self.current_user
        handler_page['bid'] = bid
        catalog_obj = Catalog.by_id(bid)
        if catalog_obj is None:
            self.send_error(404)
            return
        handler_page['book'] = catalog_obj.obj_info_view_by('basic_info', 
                                    usr=usr)
        handler_page.page_init()
        book_name = handler_page['book']['name']
        handler_page['title'] = book_name + u' - 信息 - 子曰知识谱'
        handler_page['meta_keywords'] = handler_page['book']['keywords']
        handler_page['description'] = u'知识谱' + book_name + u'信息'
        handler_page.render()
        return
