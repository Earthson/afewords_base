# coding=utf-8
from tornado.web import RequestHandler


from user import User
from generator import id_generator, index_generator

class BaseHandler(RequestHandler):

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

    @property
    def request_url(self):
        return self.request.protocol + "://" + \
                self.request.host + self.request.uri

    def get(self):
        return self.redirect("/")

    def post(self):
        result = {'kind':-1, 'info':'请您先登陆！'}
        self.write(json_encode(result));
        return

    def get_error_html(self, status_code=500, **kwargs):
        return self.write(str(status_code) + '<br/>' + str(kwargs))
