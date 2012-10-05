from basepage import BasePage, with_attr

'''
new templates will use, only for get method
'''

"""+++++ login, register, reset password, check mail, repeat mail """ 
@with_attr
class LoginPage(BasePage):
    '''
    @nologin
    @get  --- for show web page
    '''
    __template_file__ = 'afewords-login.html'
    doc = {}


@with_attr
class RegisterPage(BasePage):
    '''
    @nologin
    @get  --- for show web page
    '''
    __template_file__ = 'afewords-reg.html'
    doc = {}


@with_attr
class CheckPage(BasePage):
    '''
    @nologin
    @get 
    check email or check reset password
    '''
    __template_file__ = 'afewords-check.html'
    doc = {}


@with_attr
class ResetPage(BasePage):
    '''
    @nologin
    @get  --- for show the web page
    reset password
    '''
    __template_file__ = 'afewords-reset.html'
    doc = {}


@with_attr
class RepeatMailPage(BasePage):
    '''
    @nologin
    repeat send mail when register in afewords
    '''
    __template_file__ = ''
    doc = {}


""" ++++++++++ home page """
@with_attr
class IndexPage(BasePage):
    '''
    when we first enter afewords.com
    @get
    parameter
        blog_list: list,
            [
                {
                    'title': '',    # unicode
                    'summary': '',  # unicode
                    'content': '',  # unicode
                    'release_time': '', # unicode
                    'author':   {
                                    'uid': 'xxx',   # unicode
                                    'thumb': '',    # unicode
                                    'name': '',     # unicode
                                    'isfollow': False,  # Bollean
                                }
                },
                ...
            ]
    '''
    __template_file__ = 'afewords.html'
    doc = {
        'blog_list': [], # list, 
    }


""" ++++++++++++ for user settings """
@with_attr
class UserSettingsPage(BasePage):
    '''
    @login
    @get  --- show the page
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
                        ++++++++++++++++++++++++++++
                        [ 
                            {
                                'uid': '',      # unicode
                                'name': '',     # unicode
                                'thumb': '',    # unicode
                                'isfollow': False,  # Bollean
                            },
                            ...
                        ]
                        ++++++++++++++++++++++++++++
            follower_list: [],  # list, for follower control, decide by page(int)
                        ++++++++++++++++++++++++++++
                        as the same as follow_list
                        ++++++++++++++++++++++++++++
            draft_list: [],     # list, for draft manage, decide by page(int)
                        ++++++++++++++++++++++++++++
                        [
                            {
                                'type': 'Blog', # unicode, Blog or Comment or Other
                                'time': '',     # unicode
                                'id':'',        # unicode
                            },
                            ...
                        ]
                        ++++++++++++++++++++++++++++
            notice_list:[],     # list, for notification manage, decide by page(int)
                        ++++++++++++++++++++++++++++
                        [
                            {
                                'index': 0 , # int, for index the notification
                                'isread': False, # bollean
                                'content': '',  #unicode
                            },
                            ...
                        ]
                        ++++++++++++++++++++++++++++
            tag_list:[],        # list, for tag manage
                        ++++++++++++++++++++++++++++
                        ['tag1', 'tag2', ...]
                        ++++++++++++++++++++++++++++
            
    '''
    __template_file__ = 'afewords-settings.html'
    doc = {
        'settings_type': 'invite', # distinguish settings page, according
        # only need one parameter more, we chosed in comment
    }


""" ++++++++ for author bloger page """
@with_attr
class AuthorPage(BasePage):
    '''
    author page, contain author blog, author like, author book, author about, author follow
    @get
    parameter
        author: {
                'name': '',     # unicode
                ''
            }
        page_type:  blog | like | book | about | follow
        
        @chose_one
        blog_list: [],  # list
        like_list: [],  # list
        book_list: [],  # list
        about: {},      # dict
        follow_list: [], # list
    '''
    __template_file__ = 'afewords-bloger.html'
    doc = {
        'page_type': 'blog',
        'author':{}
        # chosed one parameter from the comment
    }


""" +++++++ for blog page """
@with_attr
class BlogPage(BasePage):
    '''
    blog page, show author blog
    @get 
    '''
    __template_file__ = 'afewords-blog.html'
    doc = {}


""" ++++++ for catalog(book) """
@with_attr
class BookPage(BasePage):
    '''
    book page, show book
    @get
    '''
    __template_file__ = 'afewords-book.html'
    doc = {}

