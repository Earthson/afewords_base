from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *
from emmongodict.emmongodict import EmMongoDict

from bson import ObjectId
from datetime import datetime

from statistics import Statistics, StatisticsDoc
from generator import *
from translator.trans import *

from authority import *

from picture import Picture
from reference import Reference
from langcode import Langcode
from tableform import Tableform
from equation import Equation

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

    @classmethod
    def reftype_trans(cls, reftype):
        cls_obj = cls_gen(reftype)
        if cls_obj is None:
            return None
        try:
            reftype = cls_obj.as_reftype
        except AttributeError:
            return None
        if reftype not in cls.ref_map:
            return None
        return reftype

    @classmethod
    def is_valid_reftype(cls, reftype):
        return cls.reftype_trans(reftype) is not None

    def get_libname(self, reftype):
        reftype = self.reftype_trans(reftype)
        if reftype is None: #illeagal reftype
            return None
        return self.ref_map[reftype]

    def refinder(self, reftype, refname):
        '''this method is required by translator, require self.ref_map'''
        when_error = '[%s:%s]' % (reftype, refname)
        reftype = self.reftype_trans(reftype)
        if reftype is None: #illeagal reftype
            return when_error
        libname = self.ref_map[reftype]
        inlib = self.sub_dict(libname)
        obj = generator(inlib[refname], reftype)
        if obj is None:
            return when_error
        return obj.view_body

    @property
    def own_data(self):
        ans = list()
        ans += cls_gen('comment').by_ids(self.comment_list.load_list())
        ans += cls_gen('picture').by_ids(self.picture_lib.values())
        ans += cls_gen('langcode').by_ids(self.langcode_lib.values())
        ans += cls_gen('equation').by_ids(self.equation_lib.values())
        ans += cls_gen('tableform').by_ids(self.tableform_lib.values())
        ans += cls_gen('tableform').by_ids(self.reference_lib.values())
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
        libname = self.get_libname(reftype)
        if libname is None:
            return False
        inlib = self.sub_dict(libname)
        alias_all = set(inlib.keys())
        if refobj.alias and refobj.alias not in alias_all:
            inlib[refobj.alias] = refobj._id
            return True
        for i in range(1, 1000):
            if str(i) not in alias_all:
                refobj.alias = str(i)
                inlib[refobj.alias] = refobj._id
                return True
        return False

    def get_ref(self, reftype, refalias):
        libname = self.get_libname(reftype)
        if libname is None:
            return None
        inlib = getattr(self, libname)
        objid = inlib[refalias]
        if not objid:
            return None
        obj = inlib.generator(objid)
        return obj

    def remove_ref(self, reftype, refalias):
        libname = self.get_libname(reftype)
        if libname is None:
            return None
        inlib = getattr(self, libname)
        objid = inlib[refalias]
        if objid:
            try:
                obj = inlib.generator(objid)
                obj.remove()
            except:
                pass
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
        'env_write_access' : bool,
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
        'env_write_access' : True,
        'abstract' : '',
        'body' : '',
        'body_version' : 0,
        'view_body' : '',
        'view_body_version' : 0,
        'lang_type' : 'afewords',
        'update_time' : datetime.now,
        'release_time' : datetime.now,
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
        'env_write_access' : True,
        'lang_type' : True,
        'release_time' : True,
        'update_time' : True,
        'body_version' : True,
        'view_body_version' : True,
        'keywords' : True,
        'tag' : True,
        'privilege' : True,
        'father_id' : False,
        'father_type' : False,
        'statistics_id' : False,
        'lib_id' : False,
        'is_posted' : True,
    }
    own_data = ['statistics', 'lib']

    def __init__(self, *args, **kwargs):
        DataBox.__init__(self, *args, **kwargs)
        self.normal_translator = normal_translator

    @property
    def translator(self):
        return ArticleTranslator(self.refinder)

    @with_user_status
    def authority_verify(self, usr=None, env=None, **kwargs):
        ret = 0
        if self.privilege == 'public':
            ret = set_auth(ret, A_READ)
        if usr is None:
            return ret
        elif self.author is not None and self.author._id == usr._id:
            ret = set_auth(ret, A_READ | A_WRITE | A_DEL)
        tmp_fa = self.father
        if tmp_fa and tmp_fa.author_id == usr._id:
            ret = set_auth(ret, A_READ | A_DEL)
        tmp_env = self.env
        if tmp_env is not None:
            tmp = tmp_env.authority_verify(usr)
            if test_auth(tmp, A_DEL):
                ret = set_auth(ret, A_DEL)
            if self.env_write_access and test_auth(tmp, A_WRITE):
                ret = set_auth(ret, A_WRITE)
        if env:
            tmp = env.authority_verify(usr)
            if test_auth(tmp, A_POST):
                ret = set_auth(ret, A_POST)
        return ret

    def refinder(self, reftype, refname):
        return self.lib.refinder(reftype, refname)

    def add_ref(self, reftype, refobj):
        self.do_update()
        return self.lib.add_ref(reftype, refobj)

    def get_ref(self, reftype, refalias):
        return self.lib.get_ref(reftype, refalias)

    def remove_ref(self, reftype, refalias):
        self.do_update()
        return self.lib.remove_ref(reftype, refalias)

    def add_to_tag(self, tagname):
        tagall = set(self.tag)
        tagall.add(tagname)
        self.tag = list(tagall)

    def remove_from_tag(self, tagname):
        tagall = set(self.tag)
        tagall.discard(tagname)
        self.tag = list(tagall)

    def do_post(self):
        self.set_propertys(is_posted=True, release_time=datetime.now())

    def do_update(self):
        self.data['update_time'] = datetime.now()
        self.data['body_version'] += 1
        self.save()

    def get_relation_to_catalog(self, catalog_obj, node_id):
        from relation import Relation
        tmp_lib = self.lib.relation_catalogs
        tmp = tmp_lib[catalog_obj.uid+'#'+node_id]
        if tmp is not None:
            return Relation.by_id(tmp)
        return None

    def add_to_catalog(self, catalog_obj, node_id):
        '''relation_obj will be returned'''
        rr = self.get_relation_to_catalog(catalog_obj, node_id)
        if rr:
            return rr #already exist
        rr = catalog_obj.recommend_article(node_id, self)
        if rr is None:
            return None
        self.lib.relation_catalogs[catalog_obj.uid+'#'+node_id] = rr._id
        return rr

    def remove_from_catalog(self, catalog_obj, node_id):
        rr = self.get_relation_to_catalog(catalog_obj, node_id)
        if not rr:
            return None
        del self.lib.relation_catalogs[catalog_obj.uid+'#'+node_id]
        if catalog_obj is not None:
            catalog_obj.remove_article(node_id, rr)

    def comments_info_view_by(self, usr=None):
        if usr:
            return [each.obj_info_view_by('comment_info_for_json', usr)
                        for each in self.comments]
        return [each.comment_info_for_json for each in self.comments] 

    @db_property
    def comments():
        def getter(self):
            from comment import Comment
            tmp = self.lib.comment_list.load_all()
            ans = Comment.by_ids(tmp)
            tmp_a = [each._id for each in ans]
            self.lib.comment_list.pull(*tuple(set(tmp) - set(tmp_a)))
            #pull ids not exist
            return ans
        return getter
    
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
            return User.by_id(self.data['author_id'])
        def setter(self, value):
            self.data['author_id'] = value._id
        return getter, setter

    @db_property
    def father():
        def getter(self):
            return generator(self.data['father_id'], self.data['father_type'])
        def setter(self, val):
            self.data['father_id'] = val._id
            self.data['father_type'] = val.__class__.__name__
        return getter, setter

    @db_property
    def env():
        def getter(self):
            return generator(self.data['env_id'], self.data['env_type'])
        def setter(self, val):
            self.data['env_id'] = val._id
            self.data['env_type'] = val.cls_name
        return getter, setter

    @db_property
    def env_obj_info():
        '''return (env_id, env_type)'''
        def getter(self):
            return (self.data['env_id'], self.data['env_type'].lower())
        return getter

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
    def body():
        def getter(self):
            return self.data['body']
        def setter(self, value):
            self.data['body'] = value
            self.data['body_version'] += 1
        return getter, setter

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
    def view_body_short():
        def getter(self):
            from aflib_utils import strip_tags
            return strip_tags(self.view_body, 200)
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

    @db_property
    def comment_count():
        def getter(self):
            return len(self.lib.comment_list)
        return getter

    def set_by_info(self, infodoc):
        info_mapper = {
            'title' : 'title',
            'body' : 'body',
            'summary' : 'abstract',
            'keywords' : 'keywords',
            'privilege' : 'privilege',
        }
        tmp = dict([(ev, infodoc[ek]) for ek, ev in info_mapper.items()])
        tmp['update_time'] = datetime.now()
        self.set_propertys(**tmp)

    #property for page
    @db_property
    def overview_info():
        def getter(self):
            return self.basic_info
        return getter

    def json_info_view_by(self, info_name='overview',
                            usr=None, env=None, **kwargs):
        ans = dict()
        ans['article_type'] = self.cls_name
        ans['aid'] = self.uid
        ans['title'] = self.title
        ans['content_short'] = self.view_body_short
        ans['update_time'] = str(self.update_time)
        ans['release_time'] = str(self.release_time)
        ans['keywords'] = self.keywords
        ans['tag_list'] = self.tag
        #ans['privilege'] = self.privilege
        author = self.author
        ans['author'] = None if author is None else author.json_info_view_by(
                        'overview', usr, env, **kwargs)
        #ans['env'] = self.env.json_info_view_by('overview', usr, env, **kwargs)
        return ans

    def obj_info_view_by(self, info_name='basic_info',
                            usr=None, env=None, **kwargs):
        ans = dict()
        ans['article_type'] = self.cls_name
        ans['aid'] = self.uid
        ans['title'] = self.title
        ans['summary'] = self.abstract
        ans['content'] = self.view_body
        ans['content_short'] = self.view_body_short
        ans['release_time'] = self.release_time
        ans['update_time'] = self.update_time
        ans['keywords'] = self.keywords
        ans['tag_list'] = self.tag
        ans['privilege'] = self.privilege
        ans['comment_count'] = self.comment_count
        ans['js_list'] = self.js_list

        ans['env'] = self.env_info

        author = self.author
        ans['author'] = None if author is None else author.obj_info_view_by(
                            'basic_info', usr, env, **kwargs)
        ans['statistics'] = self.statistics.basic_info

        if info_name in ['edit_info']:
            ans['body'] = self.body
            ans['picture_list'] = [each.basic_info for each in self.pictures]
            ans['equation_list'] = [each.basic_info 
                                        for each in self.equations]
            ans['tableform_list'] = [each.basic_info 
                                        for each in self.tableforms]
            ans['reference_list'] = [each.basic_info 
                                        for each in self.references]
            ans['langcode_list'] = [each.basic_info
                                        for each in self.langcodes]
        if info_name in ['view_info']:
            ans['recommend_list'] = [] #Todo Earthson

        ans['permission'] = auth_str(self.authority_verify(
                                            usr, env, **kwargs))
        return ans

    @db_property
    def pictures():
        def getter(self):
            from picture import Picture
            return Picture.by_ids(self.lib.picture_lib.values())
        return getter

    @db_property
    def equations():
        def getter(self):
            from equation import Equation
            return Equation.by_ids(self.lib.equation_lib.values())
        return getter

    @db_property
    def tableforms():
        def getter(self):
            from tableform import Tableform
            return Tableform.by_ids(self.lib.tableform_lib.values())
        return getter

    @db_property
    def references():
        def getter(self):
            from reference import Reference
            return Reference.by_ids(self.lib.reference_lib.values())
        return getter

    @db_property
    def langcodes():
        def getter(self):
            from langcode import Langcode
            return Langcode.by_ids(self.lib.langcode_lib.values())
        return getter

    @db_property
    def env_info():
        def getter(self):
            tmp = self.env
            return None if tmp is None else tmp.as_env
        return getter

    @db_property
    def lang_list():
        def getter(self):
           return [self.lib.langcode_lib.generator(each).lang
                for each in self.lib.langcode_lib.load_doc().values()]
        return getter

    @db_property
    def js_list():
        def getter(self):
            code_dict = {'applescript':'AppleScript','as3':'AS3','bash':'Bash','coldfusion':'ColdFusion','c++':'Cpp', 'c#':'CSharp','css':'Css','delphi':'Delphi','diff':'Diff','erlang':'Erlang','groovy':'Groovy','java':'Java', 'javafx':'JavaFX','javascript':'JScript','lisp': 'Lisp','perl':'Perl','php':'Php','plain':'Plain','python':'Python', 'ruby':'Ruby','sass':'Sass','scala':'Scala','sql':'Sql','vb':'Vb','xml':'Xml'};
            return ['shBrush'+code_dict[each]+'.js' for each in self.lang_list]
        return getter

    @db_property
    def author_url():
        def getter(self):
            from aflib_conf import main_url
            tmp_url = main_url + u'user/' + str(self.author_id)
            return ('<a href="%s">' % tmp_url) + self.author.name + '</a>'
        return getter

    @db_property
    def short_article_ref_info():
        def getter(self):
            from aflib_utils import strip_tags
            return strip_tags(self.view_body, 60) + '...' + self.author_url
        return getter

    @db_property
    def article_type_with_env():
        def getter(self):
            env_cls = cls_gen(self.env_type)
            return env_cls.first_alias + '-' + self.first_alias
        return getter
