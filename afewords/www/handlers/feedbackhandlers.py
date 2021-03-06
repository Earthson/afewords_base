# coding=utf-8
from afutils.security import *
from basehandler import *

from article.feedback import Feedback
from global_info import recent_feedbacks

class FeedbackPara(BaseHandlerPara):
    paradoc = {
        'email' : '',
        'name' : '',
        'token' : '',
        'feedback' : '',
    }

from pages.postjson import FeedbackJson

class FeedbackHandler(BaseHandler):
    def post(self):
        handler_para = FeedbackPara(self)
        handler_json = FeedbackJson(self)
        usr = self.current_user
        cookie_code = self.get_vercode()
        token = handler_para['token']
        if not usr and (token is None or token.lower() != cookie_code):
            handler_json.by_status(1)
            handler_json.write()
            return #code error 
        if usr:
            handler_para['name'] = usr.name
            handler_para['email'] = usr.email    
        if not handler_para['email'] or not is_email(handler_para['email']):
            handler_json.by_status(2)
            handler_json.write()
            return #invalid email
        if len(handler_para['feedback']) < 15:
            handler_json.by_status(3)
            handler_json.write()
            return #too short
        feedback_obj = Feedback()
        feedback_obj.set_by_info(handler_para.load_doc())
        tmp = recent_feedbacks.pop_head()
        recent_feedbacks.push(feedback_obj._id)
        tmp = Feedback.by_id(tmp)
        if tmp is not None:
            tmp.remove()
        handler_json.by_status(0)
        handler_json.write()
        return #0

from pages.af_feedpage import AFFeedbackPage
from global_info import recent_feedbacks
from article.feedback import Feedback

class AFFeedbackHandler(BaseHandler):
    def get(self):
        page = AFFeedbackPage(self)
        feedbacks = sorted(Feedback.by_ids(recent_feedbacks.get_slice(-50)))
        feedback_infos = [each.obj_info_view_by() for each in feedbacks]
        page['feedback_list'] = feedback_infos
        return page.render()
