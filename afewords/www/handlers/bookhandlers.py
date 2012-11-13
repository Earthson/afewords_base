#coding=utf-8

from basehandler import *
from pages.bookpage import BookPage, BookChapterPage, BookAboutPage, BookCatalogPage


class BookHandlerPara(BaseHandlerPara):

    paradoc = {
        #todo deju
        'edit': 'no',  # unicode, yes or not, edit book or not
        'load': 'cover',    # unicode, cover or summary or catalog
    }

    def read(self):
        BaseHandlerPara.read(self)
        if self['load'] not in ('cover', 'summary', 'catalog', 'chapter'):
            self['load'] = 'cover'
        self['edit'] = False if self['edit'] != 'yes' else True


class BookHandler(BaseHandler):
    '''
        bid get from url
    '''
    def get(self, bid):
        from article.catalog import Catalog
        handler_paras = BookHandlerPara(self)
        handler_page = BookPage(self)
        usr = self.current_user
        handler_page['bid'] = bid
        handler_page['isedit'] = handler_paras['edit']
        handler_page['load_page'] = handler_paras['load']
        catalog_obj = Catalog.by_id(bid)
        if catalog_obj is None:
            self.send_error(404)
            return
        if handler_page['isedit'] is True:
            handler_page['book'] = catalog_obj.edit_info
        else:
            handler_page['book'] = catalog_obj.obj_info_view_by('basic_info', 
                                    usr=usr)
        handler_page.page_init()
        handler_page.render()
        return


class BookAboutHandler(BaseHandler):
    '''
        bid get from url
    '''
    def get(self, bid):
        from article.catalog import Catalog
        handler_paras = BookHandlerPara(self)
        handler_page = BookAboutPage(self)
        usr = self.current_user
        handler_page['bid'] = bid
        handler_page['isedit'] = handler_paras['edit']
        handler_page['load_page'] = handler_paras['load']
        catalog_obj = Catalog.by_id(bid)
        if catalog_obj is None:
            self.send_error(404)
            return
        if handler_page['isedit'] is True:
            handler_page['book'] = catalog_obj.obj_info_view_by(
                        'edit_with_summary', usr=usr)
        else:
            handler_page['book'] = catalog_obj.obj_info_view_by('with_summary', 
                                    usr=usr)
        handler_page.page_init()
        handler_page.render()
        return

class BookCatalogHandler(BaseHandler):
    '''
        url /book/xxx/catalog
        bid get from url
    '''
    def get(self, bid):
        from article.catalog import Catalog
        handler_paras = BookHandlerPara(self)
        handler_page = BookCatalogPage(self)
        usr = self.current_user
        handler_page['bid'] = bid
        handler_page['isedit'] = handler_paras['edit']
        handler_page['load_page'] = handler_paras['load']
        catalog_obj = Catalog.by_id(bid)
        if catalog_obj is None:
            self.send_error(404)
            return
        if handler_page['isedit'] is True:
            handler_page['book'] = catalog_obj.obj_info_view_by('edit_info',
                                    usr=usr)
        else:
            handler_page['book'] = catalog_obj.obj_info_view_by('basic_info', 
                                    usr=usr)
        handler_page.page_init()
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
        handler_page['previous_chapter'] = \
                handler_page['book']['chapter_list'][pre] if pre else None
        handler_page['next_chapter'] = \
                handler_page['book']['chapter_list'][nxt] if nxt else None
        handler_page['bid'] = bid
        handler_page.page_init()
        handler_page.render()
        return
