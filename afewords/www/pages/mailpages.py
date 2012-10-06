#coding=utf-8
from basepage import BaseMail, with_attr

from tornado.escape import url_escape
from tornado.escape import xhtml_escape

@with_attr
class RegCheckMail(BaseMail):
    '''
    Registration Mail Check Page
    '''
    __template_file__ = 'reg_check_mail.html'

    subject = u'子曰--验证注册'

    doc = {
        'name' : '', #usr.name
        'mail_to' : '', #usr.email
        'token' : '',  #usr.token
    }

    def by_user(self, usr):
        self['name'] = usr.name
        self['mail_to'] = url_escape(usr.email)
        self['token'] = url_escape(usr.token)


@with_attr
class PasswordResetMail(BaseMail):
    '''
    RT:
    '''
    __template_file__ = 'password_reset_mail.html'

    subject = u'子曰--密码重置'

    doc = {
        'name' : '', #usr.name
        'mail_to' : '', #usr.email
        'token' : '', #usr.token
    }

    def by_user(self, usr):
        self['name'] = usr.name
        self['mail_to'] = url_escape(usr.email)
        self['token'] = url_escape(usr.token)

@with_attr
class InviteMail(BaseMail):
    '''
    Invite others to join afewords
    '''
    __template_file__ = 'invite_mail.html'

    subject = u'子曰--邀请注册'

    doc = {
        'invitor' : '', #invitor's name
        'invitor_id' : '', #invitor's id
        'invitee' : '', #invitee's email
    }

    def by_user(self, invitor, invitee_email):
        '''
        User: invitor
        unicode: invitee_email
        '''
        self['invitor'] = invitor.name
        self['invitor_id'] = invitor.uid
        self['invitee'] = invitee_email
