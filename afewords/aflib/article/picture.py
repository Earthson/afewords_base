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
    required_fields = ['file_name', 'thumb_name']
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

    pic_path = ''

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
            return self.pic_path + self.file_name
        return getter

    @db_property
    def thumb_url():
        def getter(self):
            return self.pic_path + self.thumb_name
        return getter
