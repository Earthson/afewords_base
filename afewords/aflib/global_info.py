from datetime import datetime
from emmongodict import EmMongoDict

class AFGlobal(EmMongoDict):
    
    db_info = {
        'db' : 'afewords',
        'collection' : 'global_info',
    }

