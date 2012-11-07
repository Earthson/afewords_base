#coding=utf-8
from basepage import with_attr, BaseJson

class StatusJson(BaseJson):
    doc = {
        'status' : 0,
        'info' : '',
    }

    error_info = {
        0 : '',
    }

    def by_status(self, status):
        self['status'] = status
        self['info'] = self.error_info[status]


_img_error_doc = {
    51 : u'不支持的图片类型',
    52 : u'上传文件过大',
    53 : u'非法图片',
    54 : u'图片长度和宽度过大',
    55 : u'请上传图片',
    56 : u'非法裁剪参数',
}

@with_attr
class LoginStatusJson(BaseJson):
    error_info = {
        0 : '',
        100 : '请先登入',
        200 : '您已经登入, 请先退出',
    }


@with_attr
class RegisterJson(StatusJson):
    '''
    @nologin
    @ajax_post
    '''
    doc = {
        'status' : 0, #status: 1 for error
        'info' : '', #error info to display, when registration error occured
    }

    error_info = {
        0 : u'注册成功',
        1 : u'请您填写正确的姓名！',
        2 : u'邮箱格式不正确！',
        3 : u'请您填写密码，至少4位！',
        4 : u'验证码错误！',
        6 : u'邮箱已经被注册！',
        7 : u'很抱歉您并未被邀请！',
        8 : u'验证邮件发送失败！',
    }


@with_attr
class ResetJson(StatusJson):
    '''
    @nologin
    @ajax_post
    '''
    error_info = {
        0 : u'请登入邮箱完成密码重置', # normal
        1 : u'请填写正确的邮箱！',
        2 : u'请您设置新密码，4位以上！',
        3 : u'邮箱尚未注册！',
        4 : u'重置密码邮件发送错误！',
    }


@with_attr
class RepeatMailJson(StatusJson):
    '''
    @nologin
    @ajax_post
    '''
    error_info = {
        0 : u'发送成功, 请登入邮箱完成验证',
        1 : u'非法调用',
        2 : u'请稍后尝试',
        3 : u'邮箱不存在',
        4 : u'邮件发送失败，请稍后再尝试',
        5 : u'您无需验证，请尝试登入或者重置密码',
    }


@with_attr
class UpdateArticleJson(StatusJson):
    '''
    @login
    @ajax_post
    '''
    doc = {
        #for new write
        'isnew': 0, # 1 for True, <=0 for False
        'article_id': '',   # unicode
    }
    error_info = {  # int info 
        0: '',
        1: u'请填写标题！',
        2: u'请填写正文！',
        3: u'无权操作他人的文章',
        4: u'文章不存在！',
        5: u'小组不存在！',
        6: u'你不是该小组成员！',
        7: u'你不是小组管理员，无权操作！',
        8: u'不支持当前操作！', 
        9: u'请先登陆！',
        10: u'非法参数!',
        11: u'不支持的文章类型',
        12: u'您无权在此创建文章',
        13: u'文章创建失败',
        14: u'非法环境参数',
        15: u'环境不匹配',
        16: u'您无权操作该文章',
        17: u'您无权在此发布',
        18: u'无法评论该对象，可能不存在',
    }

    def as_new(self, article_obj):
        self['isnew'] = 1
        self['article_id'] = article_obj.uid


@with_attr
class ArticleSrcJson(StatusJson):
    '''
    @login
    '''
    doc = {
        'article_isnew': 0, # int, 0 for False, 1 for True
        'article_id': '',   # unicode
        'src_isnew': 0, # int, 0 for False, 1 for True
        'src_alias': '',    # unicode
        'img_url' : '', #for image upload
    }    

    error_info = {
        0: '',
        1: u'请填写标题！',
        2: u'请填写正文！',
        3: u'无权操作他人的文章',
        4: u'文章不存在！',
        5: u'不支持的资源类型',
        6: u'你不是该小组成员！',
        7: u'你不是小组管理员，无权操作！',
        8: u'不支持当前操作！', 
        9: u'请先登陆！',
        10: u'非法参数!',
        11: u'不支持的文章类型',
        12: u'您无权在此创建文章',
        13: u'文章创建失败',
        14: u'非法环境参数',
        15: u'环境不匹配',
        16: u'您无权操作该文章',
        17: u'您无权在此发布',
        18: u'资源不存在',
        19: u'资源添加失败',
    }
    error_info = dict(error_info, **_img_error_doc)

    def as_new(self, article_obj):
        '''for article'''
        self['article_isnew'] = 1
        self['article_id'] = article_obj.uid

    def as_new_src(self, src_obj):
        self['src_isnew'] = 1
        self['src_alias'] = src_obj.alias



@with_attr
class GetCommentJson(StatusJson):
    '''
    @ajax_post
    @parameter
        info:
            {
                'comment_list': [], # see [[blog_list]]
            }
        comment_for_json {
            'aid' : '', #comment_id
            'content' : '', #body
            'release_time' : '',
            'author' : { }, #basic_author_info_for_json #no taglist
            'ref_comment' : '', #info for reply comment
            'permission' : '',
        }
    '''
    doc = {
        'comment_list': [], # list, see [[ blog_list ]]
    }

    error_info = {
        0 : '',
        1 : u'被评论的文章不存在',
    }


@with_attr
class ArticleRemoveJson(StatusJson):
    error_info = {
        0 : u'删除成功',
        1 : u'请登入后再尝试',
        2 : u'文章不存在',
        3 : u'错误的环境参数',
        4 : u'您没有删除权限',
    }


@with_attr
class InviteJson(StatusJson):
    error_info = {
        0 : u'成功发送邀请',
        1 : u'您没有可用的邀请名额',
        2 : u'邀请发送失败',
        3 : u'邮件地址不合法',
    }


@with_attr
class UserDomainSettingJson(StatusJson):
    error_info = {
        0 : u'设置成功',
        1 : u'已被注册，请换一个',
        2 : u'非法名称',
    }

@with_attr
class UserPasswordSettingJson(StatusJson):
    error_info = {
        0 : u'设置成功',
        1 : u'密码错误',
        2 : u'输入密码太弱',
    }

@with_attr
class UserTagRemoveJson(StatusJson):
    error_info = {
        0 : u'',
    }

@with_attr
class UserTagAddJson(StatusJson):
    error_info = {
        0 : u'',
    }

@with_attr
class UserNotiReadAllJson(StatusJson):
    error_info = {
        0 : u'',
    }

@with_attr
class UserNotiEmptyJson(StatusJson):
    error_info = {
        0 : u'',
    }

@with_attr
class UserNotiReadJson(StatusJson):
    error_info = {
        0 : u'',
    }

@with_attr
class UserNotiRemoveJson(StatusJson):
    error_info = {
        0 : u'',
    }


@with_attr
class UserAvatarUploadJson(StatusJson):
    error_info = {
        0 : u'头像上传成功',
    }
    error_info = dict(error_info, **_img_error_doc)


@with_attr
class UserAvatarCropJson(StatusJson):
    error_info = {
        0 : u'头像裁剪成功',
        1 : u'请先上传图片',
    }
    error_info = dict(error_info, **_img_error_doc)
