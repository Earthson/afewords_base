'''
A_WRITE | A_POST | A_DEL | A_MANAGE | A_READ

obj.authority_verify(usr, env, **kwargs) is a method to get permission level to spec obj

use test_auth() to judge whether you have permission
'''

A_READ = 1
A_WRITE = 1 << 2
A_POST = 1 << 3
A_DEL = 1 << 4
#A_MANAGE = 1 << 5


def set_auth(self, auth):
    return self | auth

def unset_auth(self, auth):
    return self & (~auth)

def test_auth(self, auth):
    '''
    True: if self contains all permission in auth
    '''
    return (self & auth) == auth

def with_user_status(operate):
    def wrapper(self, usr, env=None, **kwargs):
        ans = operate(self, usr, env, **kwargs)
        if usr and usr.account_status in ['limitted', 'unverified']:
            ans = unset_auth(ans, A_POST)
        return ans
    return wrapper
