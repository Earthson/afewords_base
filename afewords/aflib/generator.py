from bson import ObjectId
from bson.errors import InvalidId

def id_generator(doctype):
    def id_gen(oid):
        if doctype is None or not oid:
            return None
        try:
            data = doctype.datatype.one({'_id':ObjectId(oid)})
            if data:
                return doctype(data)
            return None
        except InvalidId:
            return None
    return id_gen

def index_generator(doctype):
    def index_gen(*args, **kwargs):
        data = doctype.datatype.find_one(*args, **kwargs)
        if data:
            return doctype(data)
        return None
    return index_gen

cls_mapper = dict()

def cls_mapper_reg(cls_obj):
    cls_mapper[cls_obj.cls_name] = cls_obj
    return cls_obj

def cls_gen(objtype):
    try:
        objtype = objtype.lower()
    except AttributeError:
        return None
    if objtype not in cls_mapper.keys():
        return None
    return cls_mapper_all[objtype]

def generator(objid, objtype):
    return id_generator(cls_gen(objtype))(objid)

def ungenerator(obj):
    return obj._id, obj.__class__.__name__
