#coding=utf-8
from basehandler import *
from pages.postjson import ArticleRemoveJson

from authority import *
from afutils.type_utils import type_trans

from generator import generator, cls_gen
from article.article import Article

class ArticleRemovePara(BaseHandlerPara):
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


class ArticleRemoveHandler(BaseHandler):
    
    def post(self):
        handler_paras = ArticleRemoveParas(self)
        handler_json = ArticleRemoveJson(self)
        usr = self.current_user
        if usr is None:
            handler_json.by_status(1)
            handler_json.write()
            return #Not Login
        article_obj = generator(handler_paras['id'],
                        type_trans(handler_paras['type']))
        if article_obj is None:
            handler_json.by_status(2)
            handler_json.write()
            return #Article Not Exist
        env = generator(handler_paras['env_id'], handler_paras['env_type'])
        auth_ans = article_obj.authority_verify(usr, env)
        if test_auth(auth_ans, A_DEL) is False:
            handler_json.by_status(4)
            handler_json.write()
            return #Delete Permission Denied
        article_obj.remove()
        handler_json.by_status(0)
        handler_json.write()
        return #0
