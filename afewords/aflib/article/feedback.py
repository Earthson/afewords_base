from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *
from emmongodict.emmongodict import EmMongoDict
from databox.mongokit_utils import with_conn

from bson import ObjectId


@with_conn
class FeedbackDoc(AFDocument):
    __collection__ = 'FeedbackDB'

    structure = {
        'email': basestring,
        'name' : basestring,
        'body' : basestring,
    }
    default_values = {
        'email' : '',
        'name' : '',
        'body' : '',
    }


@with_mapper
class Feedback(DataBox):
    datatype = FeedbackDoc

    mapper = {
        'email' : True,
        'name' : True,
        'body' : True,
    }

    def set_by_info(self, infodoc):
        ans = dict()
        ans['email'] = infodoc['email']
        ans['name'] = infodoc['name']
        ans['body'] = infodoc['feedback']
        self.set_propertys(**ans)

