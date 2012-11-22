from databox.mongokit_utils import with_conn
from databox.databox import *

from picture import PictureDoc, Picture

from datetime import datetime


@with_conn
class AvatarDoc(PictureDoc.__clsobj__):
    __collection__ = 'AvatarDB'

    default_values = {
        'name' : '',
        'alias' : '',
        'release_time' : datetime.now,
        'file_name' : '',
        'thumb_name' : '',
    }


@with_mapper
class Avatar(Picture):
    datatype = AvatarDoc

    pic_path = 'static/avatar/normal/'
    thumb_path = 'static/avatar/small/'

    @class_property
    def cls_alias(cls):
        return [u'avatar']

    @db_property
    def url():
        def getter(self):
            if not self.data['file_name']:
                return self.pic_main_url + \
                    'static/avatar/normal/afewords-user.jpg'
            return self.pic_main_url + self.pic_path + self.file_name
        return getter

    @db_property
    def thumb_url():
        def getter(self):
            if not self.data['file_name']:
                return self.pic_main_url + \
                    'static/avatar/small/afewords-user.jpg'
            return self.pic_main_url + self.pic_path + self.file_name
        return getter
