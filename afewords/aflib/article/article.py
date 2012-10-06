from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *
from emmongodict.emmongodict import EmMongoDict

from bson import ObjectId
from datetime import datetime

from statistics import Statistics, StatisticsDoc
from article_utils import *
from generator import *
from translator.trans import *

@with_conn
class ArticleLibDoc(AFDocument):
    __collection__ = 'ArticleLib'

    structure = {
        'picture_lib' : {
            #alias: _id
            basestring : ObjectId,
        },
        'langcode_lib' : {
            #alias: _id
            basestring : ObjectId,
        },
        'equation_lib' : {
            #alias: _id
            basestring : ObjectId,
        },
        'tableform_lib' : {
            #alias: _id
            basestring : ObjectId,
        },
        'reference_lib' : {
            #alias: _id
            basestring : ObjectId,
        },
        'relation_catalogs' : {
            #(catalog_id)#(node_id): _id
            basestring : ObjectId,
        },
        'comment_list' : [ObjectId], #comment_ids
    }


class ArticleLib(EmMongoDict):
    datatype = ArticleLibDoc
    db_info = {
        'db' : 'afewords',
        'collection' : 'ArticleLib',
    }

    ref_map = {
        'img' : 'picture_lib',
        'code' : 'langcode_lib',
        'math' : 'equation_lib',
        'table' : 'tableform_lib',
        'ref' : 'reference_lib',
    }

    def get_libname(self, reftype):
        if reftype not in self.ref_map.keys():
            return None
        return self.ref_map[reftype]

    def refinder(self, reftype, refname):
        '''this method is required by translator, require self.ref_map'''
        if reftype not in self.ref_map.keys(): #illeagal type
            return '[%s:%s]' % (reftype, refname)
        libname = self.ref_map[reftype]
        inlib = self.sub_dict(libname)
        obj = ref_generator(reftype, inlib[refname])
        if obj is None:
            return '[%s:%s]' % (reftype, refname)
        return obj.view_body

    @property
    def own_data(self):
        ans = []
        ans += [self.comment_list.generator(each) 
                for each in self.comment_list.load_list()]
        ans += [self.picture_lib.generator(each)
                for each in self.picture_lib.load_doc().values()]
        ans += [self.langcode_lib.generator(each)
                for each in self.langcode_lib.load_doc().values()]
        ans += [self.equation_lib.generator(each)
                for each in self.equation_lib.load_doc().values()]
        ans += [self.tableform_lib.generator(each)
                for each in self.tableform_lib.load_doc().values()]
        ans += [self.reference_lib.generator(each)
                for each in self.reference_lib.load_doc().values()]
        return ans

    @property
    def comment_list(self):
        from comment import Comment
        return self.sub_list('comment_list',
                        generator=id_generator(Comment))

    @property
    def picture_lib(self):
        from picture import Picture
        return self.sub_dict('picture_lib',
                        generator=id_generator(Picture))

    @property
    def langcode_lib(self):
        from langcode import Langcode
        return self.sub_dict('langcode_lib',
                        generator=id_generator(Langcode))

    @property
    def equation_lib(self):
        from equation import Equation
        return self.sub_dict('equation_lib',
                        generator=id_generator(Equation))

    @property
    def tableform_lib(self):
        from tableform import Tableform
        return self.sub_dict('tableform_lib',
                        generator=id_generator(Tableform))

    @property
    def reference_lib(self):
        from reference import Reference
        return self.sub_dict('reference_lib',
                        generator=id_generator(Reference))

    @property
    def relation_catalogs(self):
        from relation import Relation
        return self.sub_dict('relation_catalogs',
                        generator=None)

    def add_ref(self, reftype, refobj):
        inlib = self.sub_dict(self.get_libname(reftype))
        alias_all = inlib.keys()
        if refobj.alias and refobj.alias not in alias_all:
            inlib[refobj.alias] = refobj._id
            return True
        for i in range(1000):
            if str(i) not in alias_all:
                refobj.alias = str(i)
                inlib[refobj.alias] = refobj._id
                return True
        return False

    def remove_ref(self, reftype, refalias):
        libname = self.get_libname(reftype)
        if not libname:
            return None
        inlib = getattr(self, libname)
        objid = inlib[refalias]
        if objid:
            obj = inlib.generator(objid)
            obj.remove()
        del inlib[refalias]

@with_conn
class ArticleDoc(AFDocument):
    __collection__ = 'ArticleDB'

    structure = {
        'name' : basestring,
        'abstract' : basestring,
        'author_name' : basestring,
        'author_id' : ObjectId,
        'env_id' : ObjectId,
        'env_type' : basestring,
        'body' : basestring,
        'body_version' : int,
        'view_body' : basestring,
        'view_body_version' : int,
        'lang_type' : basestring,
        'release_time' : datetime,
        'update_time' : datetime, #last update
        'keywords' : [basestring],
        'tag' : [basestring],
        'privilege' : basestring,
        'father_id' : ObjectId,
        'father_type' : basestring,
        'statistics_id' : ObjectId,
        'lib_id' : ObjectId,
        'is_posted' : bool,
    }
    required_fields = [] #['name', 'env_id', 'env_type']
    default_values = {
        'abstract' : '',
        'body' : '',
        'body_version' : 0,
        'view_body' : '',
        'view_body_version' : 0,
        'lang_type' : 'afewords',
        'update_time' : datetime.now,
        'keywords' : [],
        'tag' : ['default'],
        'privilege' : 'public',
        'statistics_id' : Statistics.new_doc,
        'lib_id' : ArticleLib.new_doc,
        'is_posted' : False,
    }


@with_mapper
class Article(DataBox):
    datatype = ArticleDoc

    mapper = {
        'name' : True,
        'abstract' : True,
        'author_name' : True,
        'author_id' : True,
        'env_id' : False,
        'env_type' : False,
        'lang_type' : True,
        'release_time' : True,
        'update_time' : True,
        'keywords' : True,
        'tag' : True,
        'privilege' : True,
        'father_id' : False,
        'father_type' : False,
        'statistics_id' : True,
        'lib_id' : True,
        'is_posted' : True,
    }
    own_data = ['statistics', 'lib']

    def __init__(self, *args, **kwargs):
        DataBox.__init__(self, *args, **kwargs)
        self.normal_translator = normal_translator

    def __lt__(self, other):
        return self.release_time < other.release_time

    def refinder(self, reftype, refname):
        return self.lib.refinder(reftype, refname)

    def add_ref(self, reftype, refobj):
        return self.lib.add_ref(reftype, refobj)

    def add_to_tag(self, tagname):
        tagall = set(self.tag)
        tagall.add(tagname)
        self.tag = list(tagall)

    def remove_from_tag(self, tagname):
        tagall = set(self.tag)
        tagall.discard(tagname)
        self.tag = list(tagall)

    @db_property
    def title():
        def getter(self):
            return self.data['name']
        def setter(self, value):
            self.data['name'] = value
        return getter, setter

    @db_property
    def lib():
        def getter(self):
            return ArticleLib(spec={'_id':self.data['lib_id']})
        return getter

    @db_property
    def author():
        def getter(self):
            from user import User
            return User.find_one({'_id':self.data['author_id']})
        return getter

    @db_property
    def father():
        def getter(self):
            return generator(self.data['father_type'],
                        self.data['father_id'])
        def setter(self, val):
            self.data['father_id'] = val._id
            self.data['father_type'] = val.__class__.__name__
        return getter, setter

    @db_property
    def env():
        def getter(self):
            return generator(self.data['env_type'], self.data['env_id'])
        def setter(self, val):
            self.data['env_id'] = val._id
            self.data['env_type'] = val.__class__.__name__
        return getter, setter

    @db_property
    def statistics():
        def getter(self):
            data = Statistics.datatype.find_one(
                        {'_id':self.data['statistics_id']})
            if data:
                return Statistics(data)
            return None
        return getter

    @db_property
    def view_body():
        def getter(self):
            if self.data['view_body_version'] == self.data['body_version']:
                return self.data['view_body']
            self.data['view_body_version'] = self.data['body_version']
            translator = self.translator
            self.data['view_body'] = \
                    translator.translate(self.data['body'])
            return self.data['view_body'], True
        return getter

    @db_property
    def abstract():
        def getter(self):
            return self.data['abstract']
        def setter(self, value):
            self.data['abstract'] = value
        return getter, setter

    @db_property
    def abstract_viewbody():
        def getter(self):
            return self.normal_translator.translate(self.data['abstract'])
        return getter

    #property for page&json
    @db_property
    def basic_info():
        def getter(self):
            ans = dict()
            ans['title'] = self.title
            ans['summary'] = self.abstract_viewbody
            ans['content'] = self.view_body
            ans['release_time'] = str(self.release_time)
            ans['author'] = self.author.basic_info
            return ans
        return getter
