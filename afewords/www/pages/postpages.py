#coding=utf-8
from basepage import BaseJson, with_attr 

'''
pages for method post
'''

@with_attr
class LoginPostPage(BaseJson):
    '''
    @nologin
    @normal_post
    @only_redirect
    '''
    doc = {}

@with_attr
class RegisterPostPage(BaseJson):
    '''
    @nologin
    @ajax_post
    '''
    doc = {
        'status': -1,   # int, non-zero represent wrong, 0 ---right
        'info': '',     # unicode, info
    }

@with_attr
class ResetPostPage(BaseJson):
    '''
    @nologin
    @ajax_post
    '''
    doc = {
        'status': -1,   # int 
        'info': '',     # unicode
    }
    

    
