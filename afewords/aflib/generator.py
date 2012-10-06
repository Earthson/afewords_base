from bson import ObjectId

def id_generator(doctype):
    return lambda _id: doctype(doctype.datatype.one({'_id':ObjectId(_id)}))

def index_generator(doctype):
    def index_gen(*args, **kwargs):
        return doctype(doctype.datatype.one(*args, **kwargs))
    return index_gen

def generator(objid, objtype):
    from article.blog import Blog
    from article.comment import Comment
    from article.about import About
    from article.status import Status
    from article.feedback import Feedback
    from article.bulletin import Bulletin
    from article.topic import Topic

    from user import User
    from group.basicgroup import BasicGroup
    from catalog import Catalog

    types_all = {
        Blog.__name__:Blog,
        Comment.__name__:Comment,
        About.__name__:About,
        Status.__name__:Status,
        Feedback.__name__:Feedback,
        Bulletin.__name__:Bulletin,
        Topic.__name__:Topic,
        User.__name__:User,
        BasicGroup.__name__:BasicGroup,
        Catalog.__name__:Catalog,
    }

    if objtype not in types_all.keys():
        return None
    return id_generator(objtype)(objid)

def ungenerator(obj):
    return obj._id, obj.__class__.__name__
