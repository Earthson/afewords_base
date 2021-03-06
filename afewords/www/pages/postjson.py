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
class LoginStatusJson(StatusJson):
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
class VerificationMailJson(StatusJson):
    error_info = {
        0 : u'发送成功, 请登入邮箱完成验证',
        1 : u'您已经验证过了',
        2 : u'用户不存在',
        3 : u'邮件发送失败',
        5 : u'您发送邮件过于频繁',
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
        19: u'资源添加失败,可能已经达到数量上限',
    }
    error_info = dict(error_info, **_img_error_doc)

    def __init__(self, handler=None, doc=None):
        super(ArticleSrcJson, self).__init__(handler, doc)
        self.is_json = True

    def as_new(self, article_obj):
        '''for article'''
        self['article_isnew'] = 1
        self['article_id'] = article_obj.uid

    def as_new_src(self, src_obj):
        self['src_isnew'] = 1
        self['src_alias'] = src_obj.alias

    def write(self):
        ans = self.to_json()
        if self.is_json is True:
            self.handler.write(ans)
            return
        self.handler.write('<textarea>' + str(ans) + '</textarea>')


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
class GetArticleOverviewsJson(StatusJson):
    doc = {
        'article_list' : [],
    }
    error_info = {
        0 : '',
    }


@with_attr
class ObjRemoveJson(StatusJson):
    error_info = {
        0 : u'删除成功',
        1 : u'请登入后再尝试',
        2 : u'对象不存在',
        3 : u'您没有删除权限',
    }


@with_attr
class InviteJson(StatusJson):
    error_info = {
        0 : u'成功发送邀请',
        1 : u'您没有可用的邀请名额',
        2 : u'邀请发送失败',
        3 : u'邮件地址不合法',
        4 : u'系统未开放邀请',
    }

@with_attr
class UserFollowJson(StatusJson):
    error_info = {
        0 : u'',
        1 : u'用户不存在',
        2 : u'请求被拒绝',
    }

@with_attr
class UserUnfollowJson(StatusJson):
    error_info = {
        0 : u'',
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
    doc = {
        'img_url' : '', #url of uploaded img
    }
    error_info = {
        0 : u'头像上传成功',
    }
    error_info = dict(error_info, **_img_error_doc)

    def write(self):
        ans = self.to_json()
        self.handler.write('<textarea>' + str(ans) + '</textarea>')


@with_attr
class UserAvatarCropJson(StatusJson):
    error_info = {
        0 : u'头像裁剪成功',
        1 : u'头像打开失败，请尝试先上传图片',
    }
    error_info = dict(error_info, **_img_error_doc)



@with_attr
class CatalogSectionModifyJson(StatusJson):
    error_info = {
        0 : u'设置成功',
        1 : u'章节不能为空',
        2 : u'标题不能为空',
        3 : u'知识谱不存在',
        4 : u'章节不存在',
        5 : u'你无权作此操作',
    }

@with_attr
class CatalogSectionNewJson(StatusJson):
    doc = {
        'node_id' : '', #node_id of new node
    }
    error_info = {
        0 : u'添加成功',
        1 : u'章节不能为空',
        2 : u'标题不能为空',
        3 : u'知识谱不存在',
        5 : u'你无权作此操作',
    }

@with_attr
class CatalogSectionDelJson(StatusJson):
    error_info = {
        0 : u'删除成功',
        1 : u'知识谱不存在',
        2 : u'不存在的章节',
        5 : u'你无权作此操作',
    }

@with_attr
class ObjDoLikeJson(StatusJson):
    error_info = {
        0 : u'',
        1 : u'不支持的类型',
        2 : u'对象不存在',
    }

@with_attr
class RecArticleToBookJson(StatusJson):
    doc = {
        'book_title': '',
        'chapter_title': '',
        'article_title': '',
        'relation_id': '',  # new relation id to passby
    }
    error_info = {
        0 : u'',
        1 : u'文章不存在',
        2 : u'知识谱不存在',
        3 : u'章节不存在',
    }

@with_attr
class DelArticleFromBookJson(StatusJson):
    error_info = {
        0 : u'',
        1 : u'文章不存在',
        2 : u'您无权进行此操作',
    }

@with_attr
class SpecArticleToBookJson(StatusJson):
    error_info = {
        0 : u'',
        1 : u'文章不存在',
        2 : u'知识谱不存在',
        3 : u'章节不存在',
        4 : u'您无权进行此操作',
    }

@with_attr
class UnSpecArticleFromBookJson(StatusJson):
    error_info = {
        0 : u'',
        1 : u'文章不存在',
        2 : u'知识谱不存在',
        3 : u'章节不存在',
        4 : u'您无权进行此操作',
    }

@with_attr
class FeedbackJson(StatusJson):
    error_info = {
        0 : u'',
        1 : u'验证码错误',
        2 : u'邮箱不合法',
        3 : u'内容太短',
    }

@with_attr
class AFBookCreateJson(StatusJson):
    doc = {
        'about_id' : '',
    }
    error_info = {
        0 : u'知识谱创建成功',
        1 : u'请先给知识谱命名',
    }

@with_attr
class CatalogInfoModifyJson(StatusJson):
    error_info = {
        0 : u'知识谱修改成功',
        1 : u'知识谱不存在',
        2 : u'修改被拒绝，您没有需要的权限',
    }

@with_attr
class CatalogManagerAddJson(StatusJson):
    doc = {
        'new_manager': {}, #usr overview info, with: uid, name, thumb
    }
    error_info = {
        0 : u'添加管理员成功',
        1 : u'知识谱不存在',
        2 : u'不存在的用户',
        3 : u'没有可用的管理员名额',
        4 : u'添加请求被拒绝',
    }


@with_attr
class CatalogManagerDelJson(StatusJson):
    error_info = {
        0 : u'删除管理员成功',
        1 : u'知识谱不存在',
        2 : u'删除请求被拒绝',
    }
