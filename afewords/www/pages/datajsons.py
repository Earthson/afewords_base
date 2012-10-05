#coding=utf-8
from basepage import with_attr, BaseJson

class RegisterJson(BaseJson):
    doc = {
        'kind' : 0, #status: 1 for error
        'info' : '', #error info to display, when registration error occured
    }

    def set_info(self, info_type):
        temp = {
            0 : '',
            1 : '请您填写正确的姓名！',
            2 : '邮箱格式不正确！',
            3 : '请您填写密码，至少4位！',
            4 : '验证码错误！',
            6 : '邮箱已经被注册！',
            7 : '很抱歉您并未被邀请！',
            8 : '验证邮件发送失败！',
        }
        self.doc['info'] = temp[info_type]
        self.doc['kind'] = 0 if info_type == 0 else 1
