# coding=utf-8
from tornado.web import RequestHandler


from user import User
from userstat import UserStatMongo, UserStat
from generator import id_generator, index_generator

from afutils.security import *
from afutils.url_utils import url_with_para

def without_login(operate):
    def wrapper(self, *args, **kwargs):
        if self.current_user:
            self.redirect('/home')
            return
        operate(self, *args, **kwargs)
        return
    return wrapper

def with_login(operate):
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            self.redirect('/login')
            return
        operate(self, *args, **kwargs)
        return
    return wrapper

def without_login_post(operate):
    from pages.postjson import LoginStatusJson
    def wrapper(self, *args, **kwargs):
        handler_json = LoginStatusJson(self)
        if self.current_user is not None:
            handler_json.by_status(200)
            handler_json.write()
            return
        operate(self, *args, **kwargs)
        return
    return wrapper

def with_login_post(operate):
    from pages.postjson import LoginStatusJson
    def wrapper(self, *args, **kwargs):
        handler_json = LoginStatusJson(self)
        if not self.current_user:
            handler_json.by_status(100)
            handler_json.write()
            return
        operate(self, *args, **kwargs)
        return
    return wrapper

class BaseHandlerPara(object):
    paradoc = {
    }

    def __init__(self, handler):
        self.handler = handler
        self.paradoc = dict(self.paradoc)
        self.read()

    def read(self):
        self.paradoc = dict([(ek, self.handler.get_esc_arg(ek, ev))
                                    for ek, ev in self.paradoc.items()])

    def verify(self):
        return 0

    def load_doc(self):
        return self.paradoc

    def __getitem__(self, key):
        return self.paradoc[key]

    def __setitem__(self, key, value):
        self.paradoc[key] = value

from afutils.img_utils import upload_img

class IMGHandlerPara(BaseHandlerPara):
    paradoc = {
        'picture' : None, #img uploaded
    }

    def read_img(self):
        try:
            self['picture'] = self.handler.request.files['picture'][0]
        except (KeyError, IndexError) as e:
            self['picture'] = None
        if self['picture'] is None:
            self.error_code = 55
        else:
            status, info = upload_img(self['picture'])
            if status == 0:
                self['picture'] = info
            self.error_code = status

class BaseHandler(RequestHandler):
    def redirect_with_para(self, url, paradoc):
        self.redirect(url_with_para(url, paradoc))

    def get_current_user(self):
        usr_id = self.get_cookie("UI", None)
        usr_id_token = self.get_secure_cookie("UT", None)
        if usr_id is None:
            return None
        if usr_id != usr_id_token:
            self.clear_all_cookies()
            return None
        try:
            usr = id_generator(User)(usr_id)
            if self.request.remote_ip != self.get_secure_cookie('IT', None):
                self.clear_all_cookies()
                return None
        except Exception, e:
            usr = None
        return usr

    def get_userstat(self):
        from global_info import unreg_users
        usr = self.current_user
        if usr is not None:
            return usr.stat_info_doc
        stat_id = self.get_cookie('STAT', None)
        stat_id_token = self.get_secure_cookie('STATT', None)
        if stat_id is not None and stat_id_token == stat_id:
            old_stat = UserStatMongo.by_id(stat_id)
            if old_stat:
                return old_stat
        old_stat = unreg_users.pop_head()
        if old_stat is not None:
            UserStatMongo.by_id(old_stat).remove()
        new_stat = UserStatMongo()
        new_id = new_stat['_id']
        unreg_users.push(new_id)
        self.set_cookie('STAT', str(new_id), expires_days=1)
        self.set_secure_cookie('STATT', str(new_id))
        return new_stat

    @property
    def userstat(self):
        try:
            return self.__user_stat
        except:
            self.__user_stat = self.get_userstat()
            return self.__user_stat

    @property
    def request_url(self):
        return (self.request.protocol + "://" + \
                self.request.host + self.request.uri).split('?')[0]

    def get_esc_arg(self, name, default=None):
        return arg_escape(self.get_argument(name, default))

    def get_esc_args(self, name):
        return [arg_escape(each) for each in self.get_arguments(name)]

    def get_vercode(self):
        ans = self.get_secure_cookie('ver_code', None)
        self.set_secure_cookie('ver_code', random_string(20))
        return ans

    def get(self):
        return self.redirect("/")

    def post(self):
        self.redirect('/')
        return

    def get_error_html(self, status_code=500, error_info='', **kwargs):
        from pages.errorpage import BaseErrorPage
        errorpage = BaseErrorPage(self)
        errorpage['status'] = status_code
        errorpage['error_info'] = error_info
        errorpage.render()
        return
