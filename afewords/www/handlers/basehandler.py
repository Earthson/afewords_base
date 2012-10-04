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
        '''
        user = self.current_user
        if user is not None:
            AFUser = SuperUser(user)
        else:
            AFUser = None
        error_info = dict()
        error_info = kwargs
        error_info['url'] = self.request_url
        error_info['code'] = status_code
        error_info['debug'] = AFWConfig.afewords_debug
        if 'title' not in error_info:
            title = '迷路了 - 子曰'
        if "des" not in error_info:
            if status_code >=500:
                error_info['des'] = '抱歉，服务器出错！请您将这里的信息复制并作
为反馈提交给我们，我们将尽快修复这个问题！'
            else:
                error_info['des'] = "开发人员未给出具体描述！"
        if "next_url" not in error_info:
            error_info['next_url'] = '/'
        if "exc_info" not in error_info:
            if "my_exc_info" not in error_info:
                if status_code >=500:
                    error_info['exc_info'] = '抱歉，服务器出错！'
                else:
                    error_info['exc_info'] = '错误栈未传入错误输出程序！'
            else:
                error_info['exc_info'] = error_info['my_exc_info']
        if "reason" not in error_info:
            error_info['reason'] = [error_info['des']]
        if status_code >= 500:
            logging.error(error_info['exc_info'])
            logging.error('Url Error %s' % self.request.uri)


        return self.render_string("error.html", user=AFUser, title=title, error=error_info)

        '''
        pass
