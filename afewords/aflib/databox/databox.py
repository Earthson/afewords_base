from datetime import datetime

class db_property(object):
    '''an property wrapper to data(instance of DataBase)
    for auto save support
    class.data.save()  required'''
    def __init__(self, attrfunc):
        tmp = attrfunc()
        if isinstance(tmp, tuple):
            self.getter, self.setter = tmp
        else:
            self.getter, self.setter = tmp, None

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.getter is None:
            raise AttributeError, "unreadable attribute"
        ret = self.getter(obj)
        if isinstance(ret, tuple):
            if ret[1] == True:
                obj.data.save()
                ret = ret[0]
        return ret

    def __set__(self, obj, value):
        if self.setter is None:
            raise AttributeError, "can't set attribute: Unwritable"
        self.setter(obj, value)
        obj.data.save()

    @classmethod
    def get_mapper_attr(cls, name, writable=True):
        '''for basic mapper use db_propertys'''
        def attrfunc_r():
            def getter(self):
                return self.data[name]
            return getter, None
        def attrfunc_rw():
            def getter(self):
                return self.data[name]
            def setter(self, value):
                self.data[name] = value
            return getter, setter

        return cls(attrfunc_rw) if writable else cls(attrfunc_r)


class class_property(property):

    def __get__(self, cls, owner):
        def newfunc(owner, *args, **kwargs):
            return self.fget(owner, *args, **kwargs)
        return newfunc(owner)


def with_mapper(cls_obj):
    '''
    1. with cls_obj.mapper to generate db_propertys,
    2. add cls_obj to generator.cls_mapper for cls generate
    '''
    from generator import cls_mapper_reg
    cls_mapper_reg(cls_obj) #for cls_mapper
    tmp = [(ek, db_property.get_mapper_attr(ek, ev)) 
                for ek, ev in cls_obj.mapper.items()]
    for each in tmp:
        setattr(cls_obj, *each)
    return cls_obj
        

@with_mapper
class DataBox(object):
    #Document type
    datatype = None
    
    mapper = {
        #name:writable
    }
    own_data = []

    def __init__(self, data=None, attrs=None, *args, **kwargs):
        if data is None:
            data = self.datatype(*args, **kwargs)
            if not attrs:
                data.save()
        self.data = data
        if attrs:
            self.set_propertys(**attrs)
        release_time = datetime.now() #just for play

    def __lt__(self, other):
        return self.release_time > other.release_time

    def __eq__(self, other):
        try:
            return self.uid == other.uid
        except:
            return False

    def __ne__(self, other):
        try:
            return self.uid != other.uid
        except:
            return True

    @class_property
    def cls_name(cls):
        return cls.__name__.lower()

    @class_property
    def cls_alias(cls):
        '''cls_alias may be basestring or list/tuple of basestrings'''
        return cls.__name__.lower()

    @classmethod
    def new_doc(cls):
        return cls()._id

    @classmethod
    def is_exist(cls, spec):
        return cls.datatype.find_one(spec) is not None

    @staticmethod
    def is_valid_id(oid):
        from bson import ObjectId
        return ObjectId.is_valid(oid)

    @classmethod
    def find_one(cls, *args, **kwargs):
        from generator import index_generator
        return index_generator(cls)(*args, **kwargs)

    @classmethod
    def by_id(cls, uid):
        from generator import id_generator
        return id_generator(cls)(uid)

    @classmethod
    def by_ids(cls, uids):
        from bson import ObjectId
        if uids is None:
            return []
        oids = [ObjectId(each) for each in uids if ObjectId.is_valid(each)]
        datas = cls.datatype.find({'_id':{'$in':oids}})
        return [cls(data=each) for each in datas]

    @classmethod
    def by_indexes(cls, idx_name, idx_values):
        datas = cls.datatype.find({idx_name:{'$in':idx_values}})
        return [cls(data=each) for each in datas]

    def __str__(self):
        return str(self.data)

    def __unicode__(self):
        return unicode(self.data)

    def __getitem__(self, key):
        return self.get_propertys(key)[0]

    def __setitem__(self, key, value):
        self.set_propertys(**{key:value})

    def get_propertys(self, *attrnames):
        ischanged = False
        ret = []
        for ek in attrnames:
            tmp = getattr(self.__class__, ek).getter(self)
            if isinstance(tmp, tuple):
                if tmp[1] is True:
                    ischanged = True
                tmp = tmp[0]
            ret.append(tmp)
        if ischanged is True:
            self.data.save()
        return ret

    def set_propertys(self, **keyvals):
        for ek, ev in keyvals.items():
            tmp = getattr(self.__class__, ek)
            if tmp.setter:
                tmp.setter(self, ev)
            else:
                raise AttributeError, "can't set attribute: Unwritable: %s" \
                                        % ek
        self.data.save()

    def save(self):
        '''if you change a list by append, you must call save yourself'''
        self.data.save()

    @db_property
    def _id():
        def getter(self):
            return self.data['_id']
        return getter

    @db_property
    def uid():
        def getter(self):
            return unicode(self.data['_id'])
        return getter

    @db_property
    def obj_info():
        def getter(self):
            return (self._id, self.cls_name)
        return getter

    @db_property
    def obj_url():
        def getter(self):
            return ''
        return getter

    @db_property
    def main_url():
        def getter(self):
            from aflib_conf import main_url
            return main_url
        return getter

    @db_property
    def data_status():
        def getter(self):
            return self.data['data_status']
        def setter(self, value):
            self.data['data_status'] = value
        return getter, setter

    def remove(self):
        to_remove = self.get_propertys(*self.own_data)
        for each in to_remove:
            each.remove()
        self.data.remove()
