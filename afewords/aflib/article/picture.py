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
    }


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

    pic_main_url = 'http://picture.afewords.com/'
    pic_path = 'static/picture/normal/'
    thumb_path = 'static/picture/small/'

    def file_name_gen(self, pic_format, is_thumb=False):
        if is_thumb:
            return self.thumb_path+'afw_thumb_'+ \
                    str(self.data['_id'])+pic_format.lower()
        return self.pic_path+'afw_pic'+str(self.data['_id'])+pic_format.lower()

    @db_property
    def thumb_file():
        def getter(self):
            import Image
            return Image.open(self.data['thumb_name'])
        def setter(self, value):
            if not self.data['thumb_name']:
                self.data['thumb_name'] = self.file_name_gen(value.format, True)
            tmp = value.copy()
            tmp.thumbnail(200, 200)
            tmp.save(self.data['thumb_name'], value.format)
        return getter, setter

    @db_property
    def pic_file():
        def getter(self):
            import Image
            return Image.open(self.data['file_name'])
        def setter(self, value):
            if not self.data['file_name']:
                self.data['file_name'] = self.file_name_gen(value.format)
            value.save(self.data['file_name'], value.format)
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
        return getter

    @db_property
    def url():
        def getter(self):
            return self.pic_main_url + self.pic_path + self.file_name
        return getter

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
