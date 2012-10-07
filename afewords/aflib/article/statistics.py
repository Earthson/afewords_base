from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *

@with_conn
class StatisticsDoc(AFDocument):
    __collection__ = 'StatisticsDB'
    
    structure = {
        'like_count' : int,
        'up_count' : int,
        'down_count' : int,
        'report_count' : int,
        'share_count' : int,
        'view_count' : int,
    }
    default_values = {
        'like_count' : 0,
        'up_count' : 0,
        'down_count' : 0,
        'report_count' : 0,
        'share_count' : 0,
        'view_count' : 0,
    }

@with_mapper
class Statistics(DataBox):
    datatype = StatisticsDoc

    mapper = {
        'like_count' : True,
        'up_count' : True,
        'down_count' : True,
        'report_count' : True,
        'share_count' : True,
        'view_count' : True,
    }

    #property for page&json
    @db_property
    def basic_info():
        def getter(self):
            attrs = self.mapper.keys()
            return dict(zip(attrs, self.get_propertys(*attrs)))
        return getter
