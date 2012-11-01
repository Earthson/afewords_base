import re
from bson import ObjectId


_url_pattern = r'(\b(?:http|ftp|https)://(?:.*?)(?:\s|$))'
_url_rex = re.compile(_url_pattern)

def is_url(tojudge):
    ret = _url_rex.match(tojudge)
    if ret is None:
        return False
    return True

def ref_generator(reftype, ref_id):
    from picture import Picture
    from langcode import Langcode
    from equation import Equation
    from tableform import Tableform
    from reference import Reference

    mapper = {
        'img' : Picture,
        'code' : Langcode,
        'math' : Equation,
        'table' : Tableform,
        'ref' : Reference,
    }
    if reftype not in mapper.keys() or not ref_id:
        return None
    data = mapper[reftype].datatype.find_one({'_id':ObjectId(ref_id)})
    if data:
        return mapper[reftype](data)
    return None
