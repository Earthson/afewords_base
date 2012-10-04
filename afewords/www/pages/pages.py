from basepage import BasePage, with_attr

'''
new templates will use, only for get method
'''

@with_attr
class LoginPage(BasePage):
    '''
    @nologin
    '''
    __template_file__ = 'afewords-login.html'
    doc = {}

@with_attr
class RegisterPage(BasePage):
    '''
    @nologin
    '''
    __template_file__ = 'afewords-reg.html'
    doc = {}

@with_attr
class CheckPage(BasePage):
    '''
    @nologin
    check email or check reset password
    '''
    __template_file__ = 'afewords-check.html'
    doc = {}

@with_attr
class ResetPage(BasePage):
    '''
    @nologin
    reset password
    '''
    __template_file__ = 'afewords-reset.html'
    doc = {}

@with_attr
class UserSettingsPage(BasePage):
    '''
    @login
        user settings page, like invite, domain, password, avatar etc...
        parameter:
            settings_type:  invite      |   # user's invite
                            password    |   # user's domain manage
                            domain      |   # user's domain settings
                            avatar      |   # user's avatar settings
                            follow      |   # user's follow manage
                            tag         |   # user's blog taglib manage
                            follower    |   # user's follower manage
                            notice      |   # user's notifications manage
                            draft           # user's drafts manage
            invite_count: 0,    # int, for invite page
            domain: 'xxx',      # unicode, for domain page
            avatar_path: '',    # unicode, for avatar settings
            follow_list: [],    # list, for follow control, decide by page(int)
            follower_list: [],  # list, for follower control, decide by page(int)
            draft_list: [],     # list, for draft manage, decide by page(int)
            notice_list:[],     # list, for notification manage, decide by page(int)
            tag_list:[],        # list, for tag manage
            
    '''
    __template_file__ = 'afewords-settings.html'
    doc = {
        'settings_type': 'invite', # distinguish settings page, according
        # only need one parameter more, we chosed in comment
    }


