from databox.mongokit_utils import with_conn

from picture import PictureDoc, Picture


@with_conn
class AvatarDoc(PictureDoc.__clsobj__):
    __collection__ = 'AvatarDB'


class Avatar(Picture):
    datatype = AvatarDoc

    pic_path = 'static/avatar/'
