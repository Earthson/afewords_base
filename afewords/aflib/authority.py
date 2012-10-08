'''
A_WRITE | A_POST | A_DEL | A_MANAGE | A_READ

obj.authority_verify(usr, **env) is a method to get permission level to spec obj

use test_auth() to judge whether you have permission
'''

A_WRITE = 1 << 5
A_POST = 1 << 4
A_DEL = 1 << 3
A_MANAGE = 1 << 2
A_READ = 1


def set_auth(self, auth):
    return self | auth

def unset_auth(self, auth):
    return self & (~auth)

def test_auth(self, auth):
    '''
    True: if self contains all permission in auth
    '''
    return (self & auth) == auth

