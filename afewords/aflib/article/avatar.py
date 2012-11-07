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

    @db_property
    def url():
        def getter(self):
            return self.pic_main_url + 'static/avatar/normal/afewords-user.jpg'
        return getter

    @db_property
    def thumb_url():
        def getter(self):
            return self.pic_main_url + 'static/avatar/small/afewords-user.jpg'
        return getter
