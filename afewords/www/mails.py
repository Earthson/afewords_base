from pages.mailpages import *
from afutils.mail_utils import send_mail
from afconfig import af_conf

def send_invite(invitor, invitee_mail):
    mail = InviteMail()
    mail.by_user(invitor, invitee_mail)
    mail_from = af_conf['main_mail']
    return send_mail(mail_from, invitee_mail, mail.subject, str(mail))


def send_mail_pwd_reset(usr):
    mail = PasswordResetMail()
    mail.by_user(usr)
    mail_from = af_conf['main_mail']
    return send_mail(mail_from, usr.email, mail.subject, str(mail))


def send_mail_email_verification(usr):
    mail = RegCheckMail()
    mail.by_user(usr)
    mail_from = af_conf['main_mail']
    return send_mail(mail_from, usr.email, mail.subject, str(mail))
