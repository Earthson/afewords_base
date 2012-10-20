#coding=utf-8
from basehandler import *
from pages.pages import WritePage

from authority import *

def type_trans(src):
    from article.blog import Blog
    from user import User
    trans_doc = {
        'blog' : Blog.__name__,
        'user' : User.__name__,
    }
    try:
        return trans_doc[src]
    except KeyError:
        return None

class ArticleWritePara(BaseHandlerPara):
    paradoc = {
        'id': None,
        'type': 'blog',
        'env_type' : None,
        'env_id' : None,
    }

    def read(self):
        self['id'] = self.handler.get_esc_arg('id')
        self['type'] = self.handler.get_esc_arg('type', 'blog')
        self['env_type'] = self.handler.get_esc_arg('env_type', None)
        self['env_id'] = self.handler.get_esc_arg('env_id', None)


class ArticleWriteHandler(BaseHandler):
    
    @with_login
    def get(self):
        from generator import generator
        pageparas = ArticleWritePara(self)
        page = WritePage(self)
        usr = self.current_user
        page['article_type'] = pageparas['type']
        pageparas['env_type'] = type_trans(pageparas['env_type'])
        pageparas['type'] = type_trans(pageparas['type'])
        if not pageparas['type']:
            self.send_error(404, error_info=u'Invalid Article Type') #todo Earthson
            return
        if not pageparas['env_id'] and not pageparas['env_type']:
            page['owner'] = usr.as_env
            env_info = (usr._id, usr.__class__.__name__)
        else:
            env = generator(pageparas['env_id'], pageparas['env_type'])
            if not env:
                self.send_error(404, error_info=u'Invalid Envirenment')
                return
            env_info = (env.__class__.__name__, env._id)
            page['owner'] = env.as_env

        if not pageparas['id']:
            page.page_init()
            page.render()
            return
        page['isedit'] = True
        toedit = generator(pageparas['id'], pageparas['type'])
        if toedit is None:
            self.send_error(404, error_info=u'Article Not Found')
            return
        if (toedit.env_id, toedit.env_type) != env_info:
            self.send_error(404, error_info=u'Invalid Envirenment')
            return
        auth_ret = toedit.authority_verify(usr)
        if not test_auth(auth_ret, A_WRITE):
            self.send_error(404, error_info=u'Permission Denied')
            return
        page['article'] = toedit.edit_info
        page.page_init()
        page.render()
        return
