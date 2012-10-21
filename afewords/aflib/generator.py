from bson import ObjectId
from bson.errors import InvalidId

def id_generator(doctype):
    def id_gen(oid):
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

def cls_gen(objtype):
    from article.blog import Blog
    from article.comment import Comment
    from article.about import About
    #from article.status import Status
    #from article.feedback import Feedback
    #from article.bulletin import Bulletin
    #from article.topic import Topic

    from user import User
    #from group.basicgroup import BasicGroup
    #from catalog import Catalog

    types_all = {
        Blog.__name__:Blog,
        Comment.__name__:Comment,
        About.__name__:About,
    #    Status.__name__:Status,
    #    Feedback.__name__:Feedback,
    #    Bulletin.__name__:Bulletin,
    #    Topic.__name__:Topic,
        User.__name__:User,
    #    BasicGroup.__name__:BasicGroup,
    #    Catalog.__name__:Catalog,
    }

    if objtype not in types_all.keys():
        return None
    return types_all[objtype]

def generator(objid, objtype):
    return id_generator(cls_gen(obj_type))(objid)

def ungenerator(obj):
    return obj._id, obj.__class__.__name__
