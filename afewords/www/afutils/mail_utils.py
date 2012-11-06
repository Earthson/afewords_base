#coding=utf-8

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import logging
import re

_mail_rex = re.compile('^[_.0-9a-z-]+@([0-9a-z][0-9a-z-]+.)+[a-z]{2,4}$')

def validate_email(email_address):
    return _mail_rex.match(email_address) is not None


def send_mail(mail_from, mail_to, subject, html_body):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = mail_from
    msg['To'] = mail_to

    part_html = MIMEText(html_body,_subtype='html', _charset='utf-8')
    #part_text = MIMEText(text_con,'plain')
    #msg.attach(part_text)
    msg.attach(part_html)

    
    try:
        smtp = smtplib.SMTP('localhost')
        smtp.sendmail(mail_from, mail_to, msg.as_string())
        #print s.getreply()
    except smtplib.SMTPException, e:
        logging.error('+'*30)
        logging.error('Wrong: Email SMTPException')
        logging.error(e)
        logging.error('+'*30)
        smtp.quit()
        return False
    else:
        return True
