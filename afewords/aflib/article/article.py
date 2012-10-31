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

from authority import *

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

    def do_update(self):
        ans = dict()
        ans['update_time'] = datetime.now()
        ans['body_version'] += 1
        self.set_propertys(**ans)

    def add_ref(self, reftype, refobj):
        inlib = self.sub_dict(self.get_libname(reftype))
        alias_all = set(inlib.keys())
        if refobj.alias and refobj.alias not in alias_all:
            inlib[refobj.alias] = refobj._id
            self.do_update()
            return True
        for i in range(1, 1000):
            if str(i) not in alias_all:
                refobj.alias = str(i)
                inlib[refobj.alias] = refobj._id
                self.do_update
                return True
        return False

    def get_ref(self, reftype, refalias):
        libname = self.get_libname(reftype)
        if not libname:
            return None
        inlib = getattr(self, libname)
        objid = inlib[refalias]
        if not objid:
            return None
        obj = inlib.generator(objid)
        return obj

    def remove_ref(self, reftype, refalias):
        libname = self.get_libname(reftype)
        if not libname:
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
        return self.release_time > other.release_time

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
        return self.lib.add_ref(reftype, refobj)

    def get_ref(self, reftype, refalias):
        return self.lib.get_ref(reftype, refalias)

    def remove_ref(self, reftype, refalias):
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

    def comments_info_view_by(self, usr=None):
        if usr:
            return [each.obj_info_view_by('comment_info_for_json', usr)
                        for each in self.comments]
        return [each.comment_info for each in self.comments] 

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
            self.data['env_type'] = val.__class__.__name__
        return getter, setter

    @db_property
    def env_obj_info():
        '''return (env_id, env_type)'''
        def getter(self):
            return (self.data['env_id'], self.data['env_type'])
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
    def basic_info():
        def getter(self):
            ans = dict()
            ans['article_type'] = self.__class__.__name__
            ans['aid'] = self.uid
            ans['title'] = self.title
            ans['summary'] = self.abstract
            ans['content'] = self.view_body
            ans['content_short'] = self.view_body_short
            ans['release_time'] = str(self.release_time)
            tmp = self.author
            ans['author'] = None if tmp is None  else tmp.basic_info
            ans['comment_count'] = self.comment_count
            tmp = self.statistics
            ans['statistics'] = None if tmp is None else tmp.basic_info
            ans['keywords'] = self.keywords
            ans['tag_list'] = self.tag
            ans['privilege'] = self.privilege
            ans['owner'] = self.env_info
            ans['js_list'] = self.js_list
            ans['permission'] = 'r'
            return ans
        return getter

    def article_info_view_by(self, info_name='basic_info', 
                    usr=None, env=None, **kwargs):
        ans = dict()
        ans = self.get_propertys(info_name)
        try:
            ans = self.get_propertys(info_name)[0]
        except:
            return None
        ans['permission'] = auth_str(self.authority_verify(usr, env, **kwargs))
        ans['author'] = usr.as_viewer_to_uinfo(ans['author'])
        return ans

    obj_info_view_by = article_info_view_by

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
    def edit_info():
        def getter(self):
            ans = self.basic_info
            ans['body'] = self.body
            ans['picture_list'] = [each.basic_info for each in self.pictures]
            ans['equation_list'] = [each.basic_info for each in self.equations]
            ans['tableform_list'] = [each.basic_info 
                                        for each in self.tableforms]
            ans['reference_list'] = [each.basic_info 
                                        for each in self.references]
            ans['langcode_list'] = [each.basic_info
                                        for each in self.langcodes]
            return ans
        return getter

    @db_property
    def view_info():
        def getter(self):
            ans = self.basic_info
            ans['recommend_list'] = [] #Todo Earthson
            return ans
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
