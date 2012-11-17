from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *

from emmongodict.emmongodict import EmMongoDict

import time

@with_conn
class UserStatDoc(AFDocument):
    __collection__ = 'UserStatDB'

    structure = {
        'article_views' : {
            #article_id'
            basestring : {
                'type':basestring, #article_type
                'count':int, #article_view count
                'last_time':float, #last view time, gen by time.time()
            }
        }
    }
    required_fields = []
    default_values = {
        'article_views' : dict,
    }


class UserStatMongo(EmMongoDict):
    datatype = UserStatDoc

    db_info = {
        'db' : 'afewords',
        'collection' : 'UserStatDB',
    }

    @property
    def article_views(self):
        return self.sub_dict('article_views')

    def view_article(self, article_obj):
        '''try to view article'''
        view_doc = self.article_views.sub_dict(article_obj.uid)
        time_last = view_doc['last_time']
        time_now = time.time()
        if time_last is None:
            doc_new = {
                'type' : article_obj.cls_name,
                'count' : 1,
                'last_time' : time_now,
            }
            view_doc.set_all(doc_new)
            return True
        elif time_now - time_last < 2000:
            return False
        view_doc['last_time'] = time_now
        return True

@with_mapper
class UserStat(DataBox):
    datatype = UserStatDoc

    mapper = {
        'article_views' : True,
    }
