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


__cls_mapper = dict()

def cls_mapper_reg(cls_obj):
    __cls_mapper[cls_obj.cls_name] = cls_obj
    cls_alias = cls_obj.cls_alias
    if isinstance(cls_alias, basestring):
        __cls_mapper[cls_alias] = cls_obj
    elif isinstance(cls_alias, tuple) or isinstance(cls_alias, list):
        for each in cls_alias:
            __cls_mapper[each] = cls_obj
    return cls_obj

def cls_gen(objtype):
    try:
        objtype = objtype.lower()
    except AttributeError:
        return None
    if objtype not in __cls_mapper:
        return None
    return __cls_mapper[objtype]

def generator(objid, objtype):
    return id_generator(cls_gen(objtype))(objid)

def list_generator(objinfos):
    '''input list of [objid, objtype]
    output list of objs, None if not exist
    '''
    cls_map = dict()
    objs_map = dict()
    if not isinstance(objinfos, list):
        objinfos = list(objinfos)
    objinfos = [(ObjectId(each[0]), each[1])
                if each and len(each) == 2 and ObjectId.is_valid(each[0])
                else None
                    for each in objinfos]
    for each in objinfos:
        if each is None:
            continue
        tmp_cls = cls_gen(each[1])
        if tmp_cls is None:
            continue
        tmp_cls_name = tmp_cls.cls_name
        if tmp_cls_name not in cls_map:
            cls_map[tmp_cls_name] = list([each[0]])
        else:
            cls_map[tmp_cls_name].append(each[0])
    for ek, ev in cls_map.items():
        ccls = cls_gen(ek)
        tmps = [ccls(data=each) for each in ccls.datatype.find(
                    {'_id':{'$in':ev}})]
        objs_map.update((each.uid, each) for each in tmps)
    return [objs_map[str(each[0])] 
            if each and str(each[0]) in objs_map 
            else None 
                for each in objinfos]

def ungenerator(obj):
    return obj._id, obj.cls_name
