#coding=utf-8

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import logging

afewords_admin = 'afewords@afewords.com'

def send_mail(to, subject, html_con):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = afewords_admin
    msg['To'] = to

    part_html = MIMEText(html_con,_subtype='html', _charset='utf-8')
    #part_text = MIMEText(text_con,'plain')
    #msg.attach(part_text)
    msg.attach(part_html)

    
    try:
        smtp = smtplib.SMTP('localhost')
        smtp.sendmail(afewords_admin, to, msg.as_string())
        #print s.getreply()
    except smtplib.SMTPException, e:
        logging.error('+'*30)
        logging.error('Wrong: Email SMTPException')
        logging.error(e)
        logging.error('+'*30)
        smtp.quit()
        return [1, '邮件服务器出问题了！']
    else:
        return [0, '']

def send_mail_reg(to, token, name):   
    subject = u'子曰--验证注册'
    html = (u"<html><head></head><body>"
        u"<p>" + name + u"，欢迎您注册子曰，请您点击下面链接进行邮箱验证操作！</p>"
        u"<br>"
        u"<p><a href='http://www.afewords.com/check?email="+ url_escape(to)+ u"&token=" + token + u"'>验证链接</a></p><br>"
        u"<p>或者将链接复制至地址栏完成邮箱激活：http://www.afewords.com/check?email="+url_escape(to)+"&token=" + token + u"</p>"
        u"</body></html>")
    return send_mail(to, subject, html)

def send_mail_reset(to, token, name):
    subject = u'子曰--密码重置'
    html = (u"<html><head></head><body>"
            u"<p>" + name + u"，您对密码进行了重置，请您点击下面链接完成密码重置操作！</p><br>"
            u"<p><a href='http://www.afewords.com/check?type=reset&email=" + url_escape(to)+ u"&token="+ token +u"'>重置链接</a></p>"
            u"<p>或者将链接复制至地址栏完成密码重置：http://www.afewords.com/check?type=reset&email="+url_escape(to)+"&token=" + token + u"</p>"
            u"<body></html>")
    return send_mail(to, subject, html)


def send_mail_invite(to, name='子曰', email='', user_id = ''):
    subject = u'子曰--邀请注册'
    html = (u"<html><head></head><body>"
            u"<p>您的好友&nbsp;<a href='http://www.afewords.com/bloger/"+ str(user_id) +"'>" + name + 
            u"</a>&nbsp;邀请您注册<a href='http://www.afewords.com'>子曰</a></p><br/><p><a href='http://www.afewords.com/reg?email="+ to + 
            u"'>注册链接</a>或者将链接复制至地址栏进行注册：http://www.afewords.com/reg?email=" + to + "</p>"
            "</body></html>")
    return send_mail(to, subject, html)
