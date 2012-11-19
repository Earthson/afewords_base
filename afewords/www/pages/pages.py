#coding=utf-8
from basepage import BasePage, with_attr

'''
new templates will use, only for get method
'''

@with_attr
class TestPage(BasePage):
    __template_file__ = 'afewords-login.html'
    

"""+++++ login, register, reset password, check mail, repeat mail """ 
@with_attr
class LoginPage(BasePage):
    '''
    @nologin
    @get  --- for show web page
    '''
    __template_file__ = 'afewords-in/in-login.html'
    doc = {
        'subpage_type': 'login',
        'title': '登陆 - 子曰',
    }


@with_attr
class RegisterPage(BasePage):
    '''
    @nologin
    @get  --- for show web page
    '''
    __template_file__ = 'afewords-in/in-reg.html'
    doc = {
        'title': '注册 - 子曰',
        'subpage_type': 'reg',
        'blog_list' : [],   # see dataformat
    }


@with_attr
class CheckPage(BasePage):
    '''
    @nologin
    @get 
    check email or check reset password
    '''
    __template_file__ = 'afewords-check.html'
    doc = {
        'subpage_type': 'mail', # 'mail' or 'password'
        'check_type': 0,    # int , 0 for mail check, 1 for password reset
        'status': -1,   # int, describe the check code
        'info': '',     # unicode, describe the check info
        'title' : u'验证邮件/密码重置 - 子曰',
    }

    error_info = {
        0 : u'验证成功', #successful
        1 : u'用户不存在',
        2 : u'抱歉，邮箱验证失败！',
        3 : u'抱歉，密码重置失败！',
        4 : u'非法参数！',
    }

    def set_args(self, error_code=0, **kwargs):
        self['check_type'] = kwargs['check_type']
        self['status'] = 1
        self['info'] = self.error_info[error_code]


@with_attr
class ResetPage(BasePage):
    '''
    @nologin
    @get  --- for show the web page
    reset password
    '''
    __template_file__ = 'afewords-in/in-reset.html'
    doc = {
        'subpage_type': 'reset',
        'title' : u'密码重置 - 子曰',
    }



""" ++++++++++ home page """
@with_attr
class IndexPage(BasePage):
    '''
    when we first enter afewords.com
    @get
    '''
    __template_file__ = 'afewords.html'
    doc = {
        'blog_list': [], # list, 
    }




@with_attr
class WritePage(BasePage):
    '''
    @login
    @get
    '''
    __template_file__ = 'afewords-write.html'
    doc = {
        'article': {},    # see the [[ article ]] in data_format
        'isedit': False,        # bollean
        'env': {},    # dict, [[ env ]]
        'do_title': '',		# unicode
        'article_type': 'blog',	# unicode
        'page_type': 'write',
        'subpage_type': 'write',
    }

    def page_init(self):
        from toolpages import WriteTitlePage
        tmp = WriteTitlePage()
        tmp['isedit'] = self['isedit']
        tmp['env'] = self['env']
        tmp['article_type'] = self['article_type']
        print '#', tmp['article_type']
        #self['do_title'] = tmp.render_string()


""" +++++++ for blog page """
@with_attr
class BlogPage(BasePage):
    '''
    blog page, show author blog
    @get 
    '''
    __template_file__ = 'afewords-blog.html'
    doc = {
        'page_type': 'blog',
        'subpage_type': 'blog',
        'ispreview': False, # bollean 
        'article': {},    # dict, see [[article]] definition in dataformat 
        'recommend_list': [], # list, see [[blog_list]] definition in dataformat
        'islike' : False,   # bollean, islike or not
    }
