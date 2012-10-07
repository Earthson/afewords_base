#coding=utf-8
from basepage import with_attr, BaseJson

@with_attr
class RegisterJson(BaseJson):
    '''
    @nologin
    @ajax_post
    '''
    doc = {
        'status' : 0, #status: 1 for error
        'info' : '', #error info to display, when registration error occured
    }

    def set_info(self, info_type):
        temp = {
            0 : u'注册成功',
            1 : u'请您填写正确的姓名！',
            2 : u'邮箱格式不正确！',
            3 : u'请您填写密码，至少4位！',
            4 : u'验证码错误！',
            6 : u'邮箱已经被注册！',
            7 : u'很抱歉您并未被邀请！',
            8 : u'验证邮件发送失败！',
        }
        self.doc['info'] = temp[info_type]
        self.doc['status'] = 0 if info_type == 0 else 1

@with_attr
class LoginJson(BaseJson):
    '''
    @nologin
    @norrmal_post
    '''
    pass


@with_attr
class ResetJson(BaseJson):
    '''
    @nologin
    @ajax_post
    '''
    doc = {
        'status': -1,   # int
        'info': '',     # unicode
    }


@with_attr
class UpdateArticleJson(BaseJson):
    '''
    @login
    @ajax_post
    '''
    doc = {
        'status': -1,   # int
        'info': '',     # unicode
    }

@with_attr
class GetCommentJson(BaseJson):
    '''
    @ajax_post
    @parameter
        info:
            {
                'comment_list': [], # see [[blog_list]]
                'ref_comment_list':[],  # see [[blog_list]]
            }
    '''
    doc = {
        'status': -1,   # int
        'info': '' or dict, # unicode or dict, unicode for error, dict for right
    }
    
