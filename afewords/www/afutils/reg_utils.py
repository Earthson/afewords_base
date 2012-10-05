from user import User
from invitation import Invitation

from security import *
from log_utils import *
from mail_utils import *

def user_reg(email, password, sex, name):
    from afconfig import af_conf
    email = email.lower()
    if User.is_exist({'email':email}):
        return 6 #'existed user'
    if af_conf['needinvite']:
        if not Invitation.is_exist({'email':email}):
            return 7 #'not invited'
    password = encrypt(password)
    token = unicode(random_string(20), 'utf-8')
    usr = User()
    doc = {
        'email' : email,
        'sex' : sex,
        'name' : name,
        'token' : token,
        'domain' : usr.uid,
        'account_status' : 'unverified',
    }
    usr.set_propertys(**doc)
    usr.avatar.thumb_name = '/static/avatar/small/afewords-user.jpg'
    
    m_status, m_info = send_mail_reg(email, token, name)
    if m_status == 1:
        logging.error('+'*30) 
        logging.error('Email send Failed')
        logging.error('%s %s %s' % (email, token, name))
        logging.error('+'*30)
        return 8 #'mail error'
    return 0
