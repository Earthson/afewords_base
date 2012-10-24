# coding=utf-8
from basehandler import *
from pages.postjson import GetCommentJson

class CommentGetHandler(BaseHandler):

    def post(self):
        handler_json = GetCommentJson(self)
        comments_info = article_obj.comments_info_view_by(self.current_user)
        handler_json['info'] = comments_info
        handler_json.by_status(0)
        handler_json.write()
        return
