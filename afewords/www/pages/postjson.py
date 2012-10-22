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
    error_info = {
        0 : u'请登入邮箱完成密码重置', # normal
        1 : u'请填写正确的邮箱！',
        2 : u'请您设置新密码，4位以上！',
        3 : u'邮箱尚未注册！',
        4 : u'重置密码邮件发送错误！',
    }

    def by_status(self, status):
        self['status'] = 1 if status != 0 else 0
        self['info'] = self.error_info[status]


@with_attr
class RepeatMailJson(BaseJson):
    '''
    @nologin
    @ajax_post
    '''
    doc = {
        'status': -1,   # int
        'info': '',     # unicode
    }
    error_info = {
        0 : u'发送成功, 请登入邮箱完成验证',
        1 : u'非法调用',
        2 : u'请稍后尝试',
        3 : u'邮箱不存在',
        4 : u'邮件发送失败，请稍后再尝试',
        5 : u'您无需验证，请尝试登入或者重置密码',
    }

    def by_status(status):
        self['status'] = status
        self['info'] = self.error_info[status]        


@with_attr
class UpdateArticleJson(BaseJson):
    '''
    @login
    @ajax_post
    '''
    doc = {
        'status': -1,   # int
        'info': '',     # int or dict 

        'isnew': 0, # 1 for True, <=0 for False
        #for new write
        'article_id': '',   # unicode
    }
    error_info = {  # int info 
        0: '',
        1: '请填写标题！',
        2: '请填写正文！',
        3: '无权操作他人的文章',
        4: '文章不存在！',
        5: '小组不存在！',
        6: '你不是该小组成员！',
        7: '你不是小组管理员，无权操作！',
        8: '不支持当前操作！', 
        9: '请先登陆！',
        10: '非法参数!',
        11: '不支持的文章类型',
        12: '您无权在此创建文章',
        13: '文章创建失败',
        14: '非法环境参数',
        15: '环境不匹配',
        16: '您无权操作该文章',
        17: '您无权在此发布',
        18: '无法评论该对象，可能不存在',
    }

    def by_status(self, status):
        self['status'] = status
        self['info'] = self.error_info[status]

    def as_new(self, article_id):
        self['isnew'] = 1
        self['article_id'] = article_id


@with_attr
class ArticleSrcJson(BaseJson):
    '''
    @login
    '''
    doc = {
        'status': -1, # -1 for error, 0 for right
        'info': '', # error code
        'article_isnew': 0, # int, 0 for False, 1 for True
        'article_id': '',   # unicode
        'src_isnew': 0, # int, 0 for False, 1 for True
        'src_alias': '',    # unicode
    }    

    def as_new(self, article_obj):
        '''for article'''
        self['article_isnew'] = 1
        self['article_id'] = article_obj.uid

    def as_new_src(self, src_obj):
        self['src_isnew'] = 1
        self['src_alias'] = src_obj.alias

    error_info = {
        0: '',
        1: '请填写标题！',
        2: '请填写正文！',
        3: '无权操作他人的文章',
        4: '文章不存在！',
        5: '不支持的资源类型',
        6: '你不是该小组成员！',
        7: '你不是小组管理员，无权操作！',
        8: '不支持当前操作！', 
        9: '请先登陆！',
        10: '非法参数!',
        11: '不支持的文章类型',
        12: '您无权在此创建文章',
        13: '文章创建失败',
        14: '非法环境参数',
        15: '环境不匹配',
        16: '您无权操作该文章',
        17: '您无权在此发布',
        18: '资源不存在',
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
    


