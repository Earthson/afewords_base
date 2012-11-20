from connbase import *

class EmMongoList(object):
    '''
    '''
    db_info = {
        'db':'EmMongoDict',
        'collection':'EmMongoDict',
    }
    coll = None

    def __init__(self, spec, path, db=None, collection=None, generator=None):
        '''path and spec should not be None'''
        self.db_info = dict(self.db_info)
        if collection is not None:
            self.db_info['collection'] = collection
        if db is not None:
            self.db_info['db'] = db
        self.spec = spec
        self.path = path
        self.generator = None

    @staticmethod
    def is_valid_id(oid):
        from bson import ObjectId
        return ObjectId.is_valid(oid)

    @auto_coll_do
    def is_exist(self):
        '''test whether spec is in db'''
        ret = self.coll.find_one(spec_or_id=self.spec, fields={'_id':1})
        return ret is not None

    @auto_coll_do
    def ensure_exist(self):
        '''return: True, if exist before
                   False, if not exist before
        '''
        if self.is_exist() is False:
            self.coll.insert(doc_or_docs=self.spec)
            return False
        return True

    @auto_coll_do
    def __getitem__(self, key):
        '''slice is not supported yet'''
        ret = self.coll.find_one(spec_or_id=self.spec, 
                    fields={self.path:{'$slice':[key, 1]}})
        return get_dict_property(ret, self.path)[0]

    @auto_coll_do
    def __setitem__(self, key, value):
        '''slice is not supported yet'''
        pos = self.path+'.'+str(key)
        return self.coll.update(spec=self.spec, document={'$set':{pos:value}})

    @auto_coll_do
    def __delitem__(self, key):
        pos = self.path+'.'+str(key)
        return self.coll.update(spec=self.spec,
                    document={'$unset':{pos:1}})

    @auto_coll_do
    def get_slice(self, start, lim=None):
        '''mongo style slice
        if lim is None:
            start is positive:
                first start object will be return
            start is negtive:
                last start object will be return
        else:
            from start lim object will be return

            (see doc of mongodb for more help...)
        '''
        if lim is None:
            ret = self.coll.find_one(spec_or_id=self.spec,
                    fields={self.path:{'$slice':start}})
            return get_dict_property(ret, self.path)
        ret = self.coll.find_one(spec_or_id=self.spec,
                    fields={self.path:{'$slice':[start, lim]}})
        return get_dict_property(ret, self.path)

    @auto_coll_do
    def add_to_set(self, *objs):
        return self.coll.update(spec=self.spec,
                        document={'$addToSet':{self.path:{'$each':objs}}})

    @auto_coll_do 
    def push(self, *objs):
        return self.coll.update(spec=self.spec,
                        document={'$pushAll':{self.path:objs}})

    @auto_coll_do
    def pop(self):
        ret = self.coll.find_and_modify(query=self.spec, 
                update={'$pop':{self.path:1}}, 
                fields={self.path:{'$slice':[-1, 1]}})
        try:
            return get_dict_property(ret, self.path)[0]
        except:
            return None

    @auto_coll_do
    def pop_head(self):
        ret = self.coll.find_and_modify(query=self.spec, 
                update={'$pop':{self.path:-1}}, 
                fields={self.path:{'$slice':[0, 1]}})
        try:
            return get_dict_property(ret, self.path)[0]
        except:
            return None

    @auto_coll_do
    def pull(self, *objs):
        if not objs:
            return
        return self.coll.update(spec=self.spec,
                        document={'$pullAll':{self.path:objs}})

    def __len__(self):
        tmp = self.load_list()
        if tmp: return len(tmp)
        return 0

    @auto_coll_do
    def load_list(self):
        '''load list as an instance of list'''
        ret = self.coll.find_one(spec_or_id=self.spec, fields=[self.path])
        if ret: return get_dict_property(ret, self.path)
        return list()

    load_all = load_list

    @auto_coll_do
    def set_list(self, newlist):
        return self.coll.update(spec=self.spec, 
                    document={'$set':{self.path:newlist}})

    set_all = set_list

    def clear(self):
        self.set_all(list())

    @auto_coll_do
    def remove(self):
        '''remove list from db'''
        return self.coll.remove(spec_or_id=self.spec)
