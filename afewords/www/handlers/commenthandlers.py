# coding=utf-8
from basehandler import *
from pages.postjson import GetCommentJson
from afutils.type_utils import type_trans

class CommentGetPara(BaseHandlerPara):
    paradoc = {
        'env_id': '',
        'env_type': 'User',
        'article_id': '',
        'article_type': 'blog',
    }

    def read(self):
        self.paradoc = dict([(ek, self.handler.get_esc_arg(ek, ev))
                                for ek, ev in self.praradoc.items()])

class CommentGetHandler(BaseHandler):

    def post(self):
        handler_json = GetCommentJson(self)
        handler_paras = CommentGetPara(self)
        article_obj = generator(handler_paras['article_id'],
                            type_trans(handler_paras['article_type']))
        comments_info = article_obj.comments_info_view_by(self.current_user)
        handler_json['info'] = comments_info
        handler_json.by_status(0)
        handler_json.write()
        return
