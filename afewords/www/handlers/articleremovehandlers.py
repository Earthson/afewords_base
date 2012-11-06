#coding=utf-8
from basehandler import *
from pages.postjson import ArticleRemoveJson

from authority import *

from generator import generator, cls_gen
from article.article import Article

class ArticleRemovePara(BaseHandlerPara):
    paradoc = {
        'id': None,
        'type': 'blog',
    }

    def read(self):
        self['id'] = self.handler.get_esc_arg('id')
        self['type'] = self.handler.get_esc_arg('type', 'blog')


class ArticleRemoveHandler(BaseHandler):
    
    @with_login_post
    def post(self):
        handler_para = ArticleRemovePara(self)
        handler_json = ArticleRemoveJson(self)
        usr = self.current_user
        article_obj = generator(handler_para['id'], handler_para['type'])
        if article_obj is None:
            handler_json.by_status(2)
            handler_json.write()
            return #Article Not Exist
        env = article_obj.env
        auth_ans = article_obj.authority_verify(usr, env)
        if test_auth(auth_ans, A_DEL) is False:
            handler_json.by_status(4)
            handler_json.write()
            return #Delete Permission Denied
        article_obj.remove()
        handler_json.by_status(0)
        handler_json.write()
        return #0
