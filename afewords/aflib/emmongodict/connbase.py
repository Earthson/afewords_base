from pymongo import *

conn = [Connection(max_pool_size=20, network_timeout=1000)]

def reconnect(*args, **kwargs):
    try:
        conn[0].close()
    finally:
        conn[0] = Connection(*args, **kwargs)


def auto_coll_do(operate):
    '''wrapper for mongodb operation
    need:
        obj.db_info = {
                'db':db_name,
                'collection':collection_name,
            }
        obj.coll
    '''
    def wrapper(obj, *args, **kwargs):
        try:
            if obj.coll is None:
                db, coll = obj.db_info['db'], obj.db_info['collection']
                obj.coll = conn[0][db][coll]
            ret = operate(obj, *args, **kwargs)
            conn[0].end_request()
            return ret
        except errors.AutoReconnect as e:
            print(e)
            return wrapper(obj, *args, **kwargs)
    return wrapper


def get_dict_property(doc, names):
    '''property path is seperated by '.', 
    return the property from doc(dict instance)'''
    names = names.split('.', 1)
    try:
        to = doc[names[0]]
    except KeyError:
        return None
    if len(names) == 1:
        return to
    else:
        return get_dict_property(to, names[1])


def coll_inc(coll_obj, spec, key, step, **kwargs):
    return coll_obj.update(spec, {'$inc':{key:step}})


def coll_incb(coll_obj, query, key, step=1, **kwargs):
    res_dict = coll_obj.find_and_modify(query, fields={key:1},
                    update={'$inc':{key:step}}, **kwargs)
    return get_dict_property(res_dict, key)


def coll_inca(coll_obj, query, key, step=1, **kwargs):
    res_dict = coll_obj.find_and_modify(query, fields={key:1},
                    update={'$inc':{key:step}}, new=True, **kwargs)
    return get_dict_property(res_dict, key)


def coll_delete_keys(coll_obj, keys, spec, **kwargs):
    '''keys: tuple'''
    doc = dict((ek, 1) for ek in keys)
    return coll_obj.update(spec, {'$unset':doc})

