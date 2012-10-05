from afutils.security import *
from basehandler import *


class VertifyCodeHandler(BaseHandler):
    def get(self):
        '''create vertify code'''
        self.set_header('Content-Type', 'image/gif')
        [buf, code] = create_vertify_code()
        self.set_secure_cookie('ver_code', code.lower())
        self.write(buf)
        return
