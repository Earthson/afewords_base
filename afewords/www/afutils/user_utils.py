from user import User
from mails import *
from invitation import Invitation
from datetime import datetime

from security import *
from log_utils import *

from afconfig import af_conf

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
    usr = User(attrs={'email':email})
    doc = {
        'sex' : sex,
        'name' : name,
        'token' : token,
        'domain' : usr.uid,
        'account_status' : 'unverified',
    }
    usr.set_propertys(**doc)
    usr.avatar.thumb_name = '/static/avatar/small/afewords-user.jpg'
    
    m_status = send_mail_email_verification(usr)
    if m_status is False:
        logging.error('+'*30) 
        logging.error('Email send Failed')
        logging.error('%s %s %s' % (email, token, name))
        logging.error('+'*30)
        return 8 #'mail error'
    return 0


def email_verification(usr):
    '''for email changing'''
    token = unicode(random_string(20), 'utf-8')
    self.token = token
    return send_mail_email_verification(usr)


def invite_other(invitor, invitee_mail):
    from invitation import Invitation
    from mails import send_invite
    
    if not Invitation.is_exist({'email':invitee_mail}):
        gcnt = global_info['invitations_count']
        if gcnt >= af_conf['invitation_limit']:
            return 1 #invitation not available, full
        if invitor.invitations <= 0:
            return 4 #your pool is empty
        invi = Invitation(attrs={'email' : invitee_mail})
        invi.date = datetime.now()
        invi.invitor = invitor.email
        global_info.inc('invitations_count')

    invitor.invitations -= 1
    if send_invite(invitor, invitee_mail):
        return 0 #successfull
    return 2 #mail sending error


def users_info_as_viewer(viewer, info_dicts):
    '''as viewer see info of others'''
    for each in info_dicts:
        viewer.as_viewer(each)
        #each['isfollow'] = viewer.is_follow(each['uid'])
        #each['isme'] = (viewer.uid == each['uid'])
    return info_dicts
