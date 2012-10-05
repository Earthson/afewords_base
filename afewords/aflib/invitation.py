from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *

from datetime import datetime


@with_conn
class InvitationDoc(AFDocument):
    __collection__ = 'InvitationDB'

    structure = {
        'email' : basestring,
        'date' : datetime,
        'invitor' : basestring,
    }
    required_fields = ['email']
    default_values = {
        'date' : datetime.now,
        'invitor' : '',
    }


@with_mapper
class Invitation(DataBox):
    datatype = InvitationDoc

    mapper = {
        'email' : True,
        'date' : True,
        'invitor' : True,
    }
