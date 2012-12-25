#coding=utf-8

from basehandler import *
from pages.af_userpage import *

from user import User
from global_info import recent_users

class AFUserRecentHandler(BaseHandler):
    def get(self):
        handler_page = AFUserLibPage(self)
        usr = self.current_user
        try:
            usrs = sorted(User.by_ids(recent_users.get_slice(-50)))
        except Exception as e:
            print(e)
            usrs = []
        handler_page['user_list'] = [each.obj_info_view_by('basic_info',
                usr=usr, env=None) for each in usrs]
        handler_page.render()
        return #0
