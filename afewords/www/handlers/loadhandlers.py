#coding=utf-8

import re
from basehandler import *
from generator import list_generator, cls_gen

class GetArticleOverviewsPara(BaseHandlerPara):
    paradoc = {
        'toload' : [], #transform by toload[]
    }

    def read(self):
        self['toload'] = self.handler.get_esc_args('toload[]')
        self['toload'] = [each.split('##') for each in self['toload']]

from pages.postjson import GetArticleOverviewsJson

class GetArticleOverviewsHandler(BaseHandler):
    def post(self):
        handler_para = GetArticleOverviewsPara(self)
        handler_json = GetArticleOverviewsJson(self)
        usr = self.current_user
        toload = list_generator(handler_para['toload'])
        toload = [each for each in toload if each]
        toload.sort()
        handler_json['article_list'] = [each.json_info_view_by(usr)
                            for each in toload]
        handler_json.by_status(0)
        handler_json.write()
        return

