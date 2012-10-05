import hashlib
import Image, ImageDraw, ImageFont, random

from tornado.escape import url_escape
from tornado.escape import xhtml_escape

def encrypt(pwd):
    ''' first use MD5, the use SHA1, result is 40 byte '''
    result = hashlib.md5(pwd).hexdigest()
    result = hashlib.sha1(result).hexdigest()
    return result

def arg_escape(value):
    if isinstance(value, basestring):
        return xhtml_escape(value)
    return value

def create_vertify_code():
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
