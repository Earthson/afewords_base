from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *

from datetime import datetime

@with_conn
class PictureDoc(AFDocument):
    __collection__ = 'PictureDB'

    structure = {
        'name' : basestring,
        'alias' : basestring,
        'file_name' : basestring,
        'thumb_name' : basestring,
        'release_time' : datetime,
    }
    required_fields = []
    default_values = {
        'name' : '',
        'alias' : '',
        'release_time' : datetime.now,
        'file_name' : '',
        'thumb_name' : '',
    }


import aflib_conf

@with_mapper
class Picture(DataBox):
    datatype = PictureDoc

    mapper = {
        'name' : True,
        'alias' : True,
        'file_name' : True,
        'thumb_name' : True,
        'release_time' : True,
    }

    #pic_main_url = 'http://picture.afewords.com/'
    pic_main_url = aflib_conf.pic_main_url
    pic_path = 'static/picture/normal/'
    thumb_path = 'static/picture/small/'

    as_reftype = u'img' #as_reftype should also in cls_alias

    @class_property
    def cls_alias(cls):
        return [u'img', u'image']

    def set_by_info(self, infodoc):
        ans = dict()
        ans['name'] = infodoc['title']
        if infodoc['picture'] is not None:
            ans['thumb_file'] = infodoc['picture']
            ans['pic_file'] = infodoc['picture']
        self.set_propertys(**ans)

    def file_name_gen(self, pic_format, is_thumb=False):
        if is_thumb:
            return 'afw_thumb_'+ \
                    str(self.data['_id'])+'.'+pic_format.lower()
        return 'afw_pic_'+str(self.data['_id'])\
                    +'.'+pic_format.lower()

    def remove(self):
        import os
        try:
            os.remove(self.file_os_path)
        except OSError as e:
            print(e)
        try:
            os.remove(self.thumb_os_path)
        except OSError as e:
            print (e)
        DataBox.remove(self)

    @db_property
    def thumb_os_path():
        def getter(self):
            if self.data['thumb_name']:
                return self.thumb_path + self.data['thumb_name']
            return None
        return getter

    @db_property
    def file_os_path():
        def getter(self):
            if self.data['file_name']:
                return self.pic_path + self.data['file_name']
            return None
        return getter

    @db_property
    def thumb_file():
        import Image
        def getter(self):
            import Image
            f_ospath = self.thumb_os_path
            if f_ospath:
                try:
                    return Image.open(f_ospath)
                except IOError, e:
                    return None
            return None
        def setter(self, value):
            if not self.data['thumb_name']:
                self.data['thumb_name'] = self.file_name_gen(value.format, True)
            tmp = value.copy()
            tmp.thumbnail((200, 200), Image.ANTIALIAS)
            tmp.save(self.thumb_path + self.data['thumb_name'], value.format)
        return getter, setter

    @db_property
    def pic_file():
        def getter(self):
            import Image
            f_ospath = self.file_os_path
            if f_ospath:
                try:
                    return Image.open(f_ospath)
                except IOError, e:
                    print(e)
                    return None
            return None
        def setter(self, value):
            if not self.data['file_name']:
                self.data['file_name'] = self.file_name_gen(value.format)
            value.save(self.pic_path + self.data['file_name'], value.format)
        return getter, setter

    @db_property
    def view_body():
        def getter(self):
            ret = r'<div class="image" title="%s">' % (self.name)
            ret += r'<div><img src="%s" alt="%s"/></div>' % (self.url,
                                                           self.name)
            ret += r'<div class="title">%s</div>' % (self.name)
            ret += '</div>'
            return ret
            #return r'![%s](%s "%s")' % (self.name, self.url, self.name)
        return getter

    @db_property
    def url():
        def getter(self):
            if not self.data['file_name']:
                return ''
            return self.pic_main_url + self.pic_path + self.file_name
        return getter

    obj_url = url

    @db_property
    def thumb_url():
        def getter(self):
            return self.pic_main_url + self.thumb_path + self.thumb_name
        return getter

    @db_property
    def basic_info():
        def getter(self):
            ans = dict()
            ans['alias'] = self.alias
            ans['name'] = self.name
            ans['thumb_name'] = self.thumb_url
            ans['url'] = self.url
            return ans
        return getter
