from mongokit import Document
import datetime

from databox import *
from mongokit_utils import *

@with_conn
class BlogPostDoc(Document):
    '''just use like MongoKit normally'''
    __collection__ = 'blog'
    __database__ = 'blog'
    structure = {
        'title':basestring,
        'body':basestring,
        'author':basestring,
        'date_creation':datetime.datetime,
        'ranks': [int],
        'tags': [basestring],
    }
    required_fields = ['title', 'author', 'date_creation']
    default_values = {
        'ranks': [],
        'date_creation': datetime.datetime.utcnow,
    }

@with_mapper
class BlogPost(DataBox):
    datatype = BlogPostDoc

    #mapper to basic data
    mapper = {
        #name:writable
        '_id':True,
        'title':True,
        'body':True,
        'author':True,
        'date_creation':True,
        'ranks':True,
        'tags':True,
    }

    @db_property
    def avg_rank():
        def getter(self):
            sum = reduce(lambda x, y: x+y, [each for each in self.data['ranks']])
            return sum / len(self.data['ranks'])
        return getter, None


a = BlogPost()
a.set_propertys(title='fdasfas', author='earthson')
a.title = 'hello world!'
a.tags = ['Programming']
print a
a.ranks.append(53)
a.ranks.append(35)
a.ranks.append(32)
a.save() #manully save, append will not auto call save operation
b = BlogPost(BlogPost.datatype.find_one({'_id':a._id}))
print b
print '##', b.avg_rank

#if you run 
#b.avg_rank = 324
