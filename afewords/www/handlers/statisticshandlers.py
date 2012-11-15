#coding=utf-8

from basehandler import *
from generator import *

class ArticleDoLikePara(BaseHandlerPara):
    paradoc = {
        'obj_id' : '',
        'obj_type' : '',
    }

from pages.postjson import ArticleDoLikeJson

class ArticleDoLikeHandler(BaseHandler):
    @with_login_post
    def post(self):
        handler_json = ArticleDoLikeJson
        usr = self.current_user
        article_obj = generator(handler_para['obj_id'], 
                                handler_para['obj_type'])
        if article_obj is None:
            handler_json.by_status(2)
            handler_json.write()
            return #article not exist
        if not usr.reverse_like_post(article_obj):
            handler_json.by_status(1)
            handler_json.write()
            return #not an article type
        handler_json.by_status(0)
        handler_json.write()
        return #0
        
