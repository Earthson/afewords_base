from datetime import datetime
from databox.databox import *
from databox.mongokit_utils import with_conn
from emmongodict import EmMongoDict

class AFGlobal(EmMongoDict):
    
    db_info = {
        'db' : 'afewords',
        'collection' : 'global_info',
    }


@with_conn
class AFGlobalDoc(AFDocument):
    __collection__ = 'global_info'

    structure = {
        'invitations_count' : int,
    }
    default_values = {
        'invitations_count' : 0,
    }

if AFGlobalDoc.find_one() is None:
    glo = AFGlobalDoc()
    glo.save()

global_info = AFGlobal(spec={'_id':AFGlobalDoc.find_one()['_id']})
