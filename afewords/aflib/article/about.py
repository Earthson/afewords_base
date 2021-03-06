from databox.mongokit_utils import with_conn
from databox.databox import *

from article import ArticleDoc, Article

from generator import cls_gen

@with_conn
class AboutDoc(ArticleDoc.__clsobj__):
    __collection__ = 'AboutDB'


@with_mapper
class About(Article):
    datatype = AboutDoc
