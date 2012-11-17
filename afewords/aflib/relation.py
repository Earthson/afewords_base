from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *

from generator import *


@with_conn
class RelationDoc(AFDocument):
    __collection__ = 'RelationDB'

    structure = {
        'relation_set' : list,
        'relation_type' : basestring,
        'up_count' : int,
        'down_count' : int,
        'activity' : int,
    }
    required_fields = []
    default_values = {
        'relation_set' : list,
        'relation_type' : '',
        'up_count' : 0,
        'down_count' : 0,
        'activity' : 0,
    }


@with_mapper
class Relation(DataBox):
    datatype = RelationDoc

    mapper = {
        'relation_set' : True,
        'relation_type' : True,
        'up_count' : True,
        'down_count' : True,
        'activity' : True,
    }

    def __init__(self, data=None, *args, **kwargs):
        DataBox.__init__(self, data, *args, **kwargs)

    def authority_verify(self, usr, **env):
        ret = 0
        if usr == None:
            ret = set_auth(ret, A_READ)
        ret |= BaseClass.authority_verify(self, user, **env)
        return ret

    def set_relation_set(self, *objs):
        tmp = [ungenerate(each) for each in objs]
        self.relation_set = tmp

    def get_relation_set_objs(self):
        return [generate(each) for each in self.relation_set]
