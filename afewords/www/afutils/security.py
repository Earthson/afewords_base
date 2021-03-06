#coding=utf-8
import re
import hashlib
import string
import Image, ImageDraw, ImageFont, random

from tornado.escape import url_escape
from tornado.escape import xhtml_escape

def encrypt(pwd):
    ''' first use MD5, the use SHA1, result is 40 byte '''
    result = hashlib.md5(pwd).hexdigest()
    result = hashlib.sha1(result).hexdigest()
    return result

def random_string(num):
    ''' num is the nums of random string '''
    salt = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return salt

def is_email(email):
    from afutils.mail_utils import validate_email
    return validate_email(email)

def arg_escape(value):
    if isinstance(value, basestring):
        return xhtml_escape(value)
    return value

def user_login(email, pwd):
    '''return user obj if successfully login'''
    from user import User
    email = email.lower()
    data = User.datatype.find_one({'email':email})
    if not data:
        return None, 1, 'User not exist'
    usr = User(data)
    pwd = encrypt(pwd)
    if usr.password != pwd:
        return None, 2, 'password error'
    return usr, 0, ':)'
    

def create_vertify_code():
    import StringIO
    background = (random.randrange(230,255),random.randrange(230,255),random.randrange(230,255))
    line_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    img_width = 90
    img_height = 30
    font_color = ['black','darkblue','darkred','red','blue','green']
    font_size = 18
    font = ImageFont.truetype(r'FreeSans.ttf',font_size)
    #font = ImageFont(font_size)
    #font = ImageFont.truetype("arial.ttf", 15)
    #request.session['verify'] = ''
    #新建画布
    im = Image.new('RGB',(img_width,img_height),background)
    draw = ImageDraw.Draw(im)
    code = random_string(6)
    #新建画笔
    draw = ImageDraw.Draw(im)
    for i in range(random.randrange(7,9)):
        xy = (random.randrange(0,img_width),random.randrange(0,img_height),random.randrange(0,img_width),random.randrange(0,img_height))
        draw.line(xy,fill=line_color,width=1)
        #写入验证码文字
    x = 4
    for i in code:
        y = random.randrange(0,10)
        draw.text((x,y), i,font=font, fill=random.choice(font_color))
        x += 14
    del x
    del draw
    buf = StringIO.StringIO()
    im.save(buf,'gif')
    buf.closed
    return [buf.getvalue(),"".join(code)]
