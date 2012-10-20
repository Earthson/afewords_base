#coding=utf-8

from basehandler import *
from pages.pages import WritePage

def type_trans(src):
    from article.blog import Blog
    trans_doc = {
        'blog' : Blog.__name__,
    }
    try:
        return trans_doc[src]
    except KeyError:
        return None

class ArticleWritePara(BaseHandlerPara):
    paradoc = {
        'id': None,
        'type': 'blog',
    }

    def read(self):
        self['id'] = self.handler.get_esc_arg('id')
        self['type'] = self.handler.get_esc_arg('type', 'blog')
        self['type'] = type_trans(self['type'])


class ArticleWriteHandler(BaseHandler):
    
    @with_login
    def get(self):
        from generator import generator
        pageparas = ArticleWritePara(self)
        page = WritePage(self)
        if not pageparas['id']:
            page.render()
            return
        if not pageparas['type']:
            self.send_error(404, u'Invalid Article Type') #todo Earthson
            return
        toedit = generator(pageparas['id'], pageparas['type'])
        if toedit is None:
            self.send_error(404, u'Article Not Found')
            return
        usr = self.current_user
        auth_ret = todeit.authority_verify(usr)
        if not test_auth(auth_ret, A_WRITE):
            self.send_error(404, u'Permission Denied')
            return
        page['article'] = toedit.edit_info
        page.render()
        return
