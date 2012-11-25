from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *
from emmongodict.emmongodict import EmMongoDict

from bson import ObjectId
from datetime import datetime

from statistics import Statistics
from about import About
from generator import *
from relation import Relation

from authority import *


@with_conn
class CatalogLibDoc(AFDocument):
    __collection__ = 'CatalogLibDB'

    structure = {
        'feedback_list' : [ObjectId],
        'topic_list' : [ObjectId],
        'relations_list' : [ObjectId],

        'node_lib' : {
            #node_id
            basestring : {
                'title' : basestring,
                'section' : basestring,
                'article_count' : int,
                'subcatalog_count' : int,
                'spec_count' : int,
            }
        },
        'node_info_lib' : {
            #node_id
            basestring : {
                #'default' : ObjectId,
                'main' : [ObjectId],
                'articles' : [ObjectId],
                'catalogs' : [ObjectId],
            }
        },
        'parent_catalogs' : {
            #(catalog_id)#(node_id) : _id
            basestring : ObjectId,
        },
    }


class CatalogLib(EmMongoDict):
    datatype = CatalogLibDoc

    db_info = {
        'db' : 'afewords',
        'collection' : 'CatalogLibDB',
    }

    @property
    def own_data(self):
        ans = list()
        ans += [each for each in 
                Relation.by_ids(self.relations_list.load_all())]
        return ans

    @property
    def parent_catalogs(self):
        return self.sub_dict('parent_catalogs')

    @property
    def feedback_list(self):
        from feedback import Feedback
        return self.sub_list('feedback_list')

    @property
    def topic_list(self):
        from topic import Topic
        return self.sub_list('topic_list')

    @property
    def node_lib(self):
        return self.sub_dict('node_lib')

    @property
    def node_info_lib(self):
        return self.sub_dict('node_info_lib')

    @property
    def relations_list(self):
        return self.sub_list('relations_list')


@with_conn
class CatalogDoc(AFDocument):
    __collection__ = 'CatalogDB'

    structure = {
        'name' : basestring,
        'owner_id' : ObjectId,
        'owner_type' : basestring,
        'managers' : [ObjectId], #User id
        'node_count' : int,
        'remove_count' : int,
        'complete_count' : int,
        'release_time' : datetime,
        'update_time' : datetime,
        'keywords' : [basestring],
        'about_id' : ObjectId,
        'statistics_id' : ObjectId,
        'lib_id' : ObjectId,
    }
    required_fields = []
    default_values = {
        'name' : '',
        'managers' : [],
        'node_count' : 0,
        'remove_count' : 0,
        'complete_count' : 0,
        'release_time' : datetime.now,
        'update_time' : datetime.now,
        'keywords' : [],
        'about_id' : None,
        'statistics_id' : Statistics.new_doc,
        'lib_id' : CatalogLib.new_doc,
    }


@with_mapper
class Catalog(DataBox):
    datatype = CatalogDoc

    mapper = {
        'name' : True,
        'owner_id' : False,
        'owner_type' : False,
        'managers' : True,
        'node_count' : True,
        'remove_count' : True,
        'complete_count' : True,
        'release_time' : True,
        'update_time' : True,
        'keywords' : True,
        'about_id' : False,
        'statistics_id' : False,
    }
    own_data = ['statistics', 'about', 'lib']

    def __init__(self, data=None, *args, **kwargs):
        DataBox.__init__(self, data, *args, **kwargs)
        if data is None:
            self.about.set_propertys(env=self, author_id=self.data['owner_id'])

    def do_update(self):
        self.update_time = datetime.now()

    @class_property
    def cls_alias(cls):
        return 'book'

    @db_property
    def statistics():
        def getter(self):
            ans = Statistics.by_id(self.data['statistics_id'])
            if ans is None:
                ans = Statistics()
                self.data['statistics_id'] = ans._id
                return ans, True
            return ans
        def setter(self, value):
            self.data['statistics_id'] = value._id
        return getter, setter

    @db_property
    def about():
        '''introduction page to user'''
        def getter(self):
            ans = About.by_id(self.data['about_id'])
            if ans is None:
                ans = About()
                self.data['about_id'] = ans._id
                ans.set_propertys(author_id=self.data['owner_id'], env=self)
                return ans, True
            if not ans.author_id or not ans.env_id or not ans.env_type:
                ans.set_propertys(author_id=self.data['owner_id'], env=self)
            return ans
        def setter(self, value):
            self.data['about_id'] = value._id
        return getter, setter

    @db_property
    def lib():
        def getter(self):
            return CatalogLib(spec={'_id':self.data['lib_id']})
        return getter

    @db_property
    def owner():
        def getter(self):
            return generator(self.data['owner_id'], self.data['owner_type'])
        def setter(self, value):
            self.data['owner_type'] = value.__class__.__name__
            self.data['owner_id'] = value._id
        return getter, setter

    @db_property
    def node_sum():
        def getter(self):
            return self.data['node_count'] - self.data['remove_count']
        return getter

    def is_manager(self, usr):
        if usr is None:
            return False
        if self.is_owner(usr) or usr._id in self.managers:
            return True
        return False

    def is_owner(self, usr):
        if usr is None:
            return False
        if self.owner_id == usr._id and \
                    self.owner_type == usr.__class__.__name__:
            return True
        return False

    @with_user_status
    def authority_verify(self, usr, env=None, **kwargs):
        ret = 0
        if usr == None:
            ret = set_auth(ret, A_READ)
        elif self.is_manager(usr):
            ret = set_auth(ret, A_READ | A_WRITE | A_DEL | A_POST)
        else:
            ret = set_auth(ret, A_READ | A_POST)
        return ret

    def spec_article_to(self, node_id, rel_obj):
        tmp = self.get_node_list(node_id, 'main')
        tmp_all = tmp.load_all()
        if tmp_all is None:
            return False
        if rel_obj._id in tmp_all:
            return True
        if not tmp_all:
            self.complete_count += 1
        #tmp.push(rel_obj._id)
        tmp.set_all([rel_obj._id])
        #self.get_node_dict(node_id)['spec_count'] += 1
        self.get_node_dict(node_id)['spec_count'] = 1
        self.do_update()
        return True

    def unspec_article_to(self, node_id, rel_obj):
        tmp = self.get_node_list(node_id, 'main')
        tmp_all = tmp.load_all()
        if tmp_all is None:
            return False
        tmpset = set(tmp_all)
        if rel_obj._id in tmpset:
            tmpset.discard(rel_obj._id)
            if len(tmpset) == 0:
                self.complete_count -= 1
            tmp.set_list(list(tmpset))
            self.get_node_dict(node_id)['spec_count'] -= 1
        self.do_update()
        return True

    def recommend_article(self, node_id, article_obj):
        if self.get_node_dict(node_id)['title'] is None:
            return None
        rr = Relation(attrs={"relation_type":"catalog-%s" % \
                            article_obj.cls_name})
        rr.set_relation_set(self, article_obj)
        tmp_list = self.get_node_list(node_id, 'articles')
        tmp_list.push(rr._id)
        self.lib.relations_list.push(rr._id)
        self.get_node_dict(node_id)['article_count'] += 1
        self.do_update()
        return rr

    def remove_article(self, node_id, rel_obj):
        self.lib.relations_list.pull(rel_obj._id)
        self.unspec_article_to(node_id, rel_obj)
        tmp_list = self.get_node_list(node_id, 'articles')
        if rel_obj._id in tmp_list:
            tmp_list.pull(rel_obj._id)
            self.get_node_dict(node_id)['article_count'] -= 1
        rel_obj.remove()

    def recommend_subcatalog(self, node_id, subcatalog_obj):
        rr = Relation(attrs={"relation_type":"catalog-%s" % \
                            subcatalog_obj.__class__.__name__})
        rr.set_relation_set(self, subcatalog_obj)
        tmp = self.get_node_list(node_id, 'catalogs')
        tmp.push(rr._id)
        self.lib.relations_list.push(rr._id)
        self.get_node_dict(node_id)['subcatalog_count'] += 1
        self.do_update()
        return rr

    def remove_subcatalog(self, node_id, rel_obj):
        self.lib.relations_list.pull(rel_obj._id)
        self.get_node_list(node_id, 'catalogs').pull(rel_obj._id)
        self.get_node_dict(node_id)['subcatalog_count'] -= 1
        rel_obj.remove()

    def add_node(self, title, section):
        tmp_node = {
            'title':title,
            'section':section,
            'article_count':0,
            'subcatalog_count':0,
            'spec_count':0,
        }
        tmp_info = {
            #'default' : None,
            'main':list(),
            'articles':list(),
            'catalogs':list(),
        }
        self.lib.node_lib[str(self.node_count)] = tmp_node
        self.lib.node_info_lib[str(self.node_count)] = tmp_info
        self.node_count += 1
        self.do_update()
        return str(self.node_count - 1)

    def modify_node(self, node_id, title, section):
        cnode = self.lib.node_lib.sub_dict(node_id)
        if cnode['title'] is None:
            return False #node not exist
        cnode['title'] = title
        cnode['section'] = section
        self.do_update()
        return True
        
    def remove_node(self, node_id):
        if not self.lib.node_lib.sub_dict(node_id).load_all():
            return False #node not exist
        tmp_rel_ids = self.get_node_list(node_id, 'articles').load_all()
        self.lib.relations_list.pull(*tuple(tmp_rel_ids))
        rels = Relation.by_ids(tmp_rel_ids)
        for each in rels:
            each.remove()
        tmp_rel_ids = self.get_node_list(node_id, 'catalogs').load_all()
        self.lib.relations_list.pull(*tuple(tmp_rel_ids))
        self.remove_count += 1
        if self.get_node_list(node_id, 'main').load_all() != []:
            self.complete_count -= 1
        rels = Relation.by_ids(tmp_rel_ids)
        for each in rels:
            each.remove()
        del self.lib.node_lib[node_id]
        del self.lib.node_info_lib[node_id]
        self.do_update()
        return True

    def get_node_dict(self, node_id):
        tmp_path = 'node_lib'+'.'+str(node_id)
        return self.lib.sub_dict(tmp_path)

    def get_node_list(self, node_id, listname):
        listname = '.'+str(listname)
        tmp_path = 'node_info_lib'+'.'+str(node_id)+listname
        return self.lib.sub_list(tmp_path)

    def add_to_catalog(self, catalog_obj, node_id):
        '''relation_obj will be returned'''
        tmp_lib = self.lib.parent_catalogs
        tmp = tmp_lib[str(catalog_obj._id)+'#'+node_id]
        if tmp is not None:
            return Relation(_id=tmp)
        rr = catalog_obj.recommend_subcatalog(node_id, self)
        tmp_lib[str(catalog_obj._id)+'#'+node_id] = rr._id
        return rr

    def remove_from_catalog(self, catalog_obj, node_id, relation_obj):
        del self.lib.parent_catalogs[str(catalog_obj._id)+'#'+node_id]
        catalog_obj.remove_subcatalog(node_id, relation_obj)

    def get_relations_from_node(self, lib_type, node_id):
        '''lib_type: articles, main, catalogs'''
        from relation import Relation
        rids = self.lib.node_info_lib.\
            sub_dict(node_id).sub_dict(lib_type).load_all()
        return Relation.by_ids(rids)

    def get_articles_from_relations(self, relations):
        '''lib_type: articles, main'''
        return list_generator([each_rel.relation_set[1] 
                                for each_rel in relations])

    def get_relations_info_from_node_view_by(self, lib_type, node_id, 
                usr=None, env=None):
        rels = self.get_relations_from_node(lib_type, node_id)
        if not rels:
            return list()
        articles = self.get_articles_from_relations(rels)
        for rel, earticle in zip(rels, articles):
            if earticle is None:
                self.remove_article(node_id, erel)
        default_id = self.get_node_list(node_id, 'main').load_all()
        if default_id:
            default_id = default_id[0]
        else:
            default_id = None
        return sorted([dict(
                    entity=earticle.obj_info_view_by('basic_info', usr, env),
                    up_count=erel.up_count,
                    down_count=erel.down_count,
                    activity=erel.activity,
                    rid=erel.uid,
                    release_time=erel.release_time,
                    is_default=False if erel._id != default_id else True,
                    ) for erel, earticle in zip(rels, articles) if earticle],
                key=lambda it:it['activity'], reverse=True)

    def get_node_info_view_by(self, node_id, usr=None, env=None):
        snode = self.lib.node_lib.sub_dict(node_id).load_all()
        if not snode:
            return None
        ans = dict()
        ans['cid'] = node_id
        ans['title'] = snode['title']
        ans['chapter_num'] = snode['section']
        ans['article_count'] = snode['article_count']
        ans['spec_article_count'] = snode['spec_count']
        ans['subcatalog_count'] = snode['subcatalog_count']
        ans['article_list'] = self.get_relations_info_from_node_view_by(
                                    'articles', node_id, usr, env)
        ans['spec_article_list'] = self.get_relations_info_from_node_view_by(
                                    'main', node_id, usr, env)
        ans['subcatalog_list'] = list()
        return ans

    @db_property
    def node_list_info():
        def getter(self):
            from aflib_utils import section_cmp
            nodes = self.lib.node_lib.load_all()
            nodeinfos = self.lib.node_info_lib.load_all()
            def trans_each(nid):
                ans = dict()
                ans['cid'] = nid
                ans['title'] = nodes[nid]['title']
                ans['chapter_num'] = nodes[nid]['section']
                ans['article_count'] = nodes[nid]['article_count']
                ans['spec_article_count'] = nodes[nid]['spec_count']
                ans['subcatalog_count'] = nodes[nid]['subcatalog_count']
                ans['article_list'] = list() #todo Earthson
                ans['spec_article_list'] = list()
                ans['subcatalog_list'] = list()
                return ans
            ans = [trans_each(each) for each in nodes.keys()]
            return sorted(ans, cmp=lambda x, y : \
                        section_cmp(x['chapter_num'], y['chapter_num'])) 
        return getter

    @db_property
    def complete_rate():
        def getter(self):
            if self.data['complete_count'] == 0:
                return 0
            return int(self.data['complete_count'] * 100 / self.node_sum)
        return getter

    #property for page&json
    def obj_info_view_by(self, info_name='basic_info', 
                            usr=None, env=None, **kwargs):
        '''
        info_name: ['basic_info', 'overview_info', 'with_summary', 'edit_info',
            'edit_with_summary']
        '''
        ans = dict()
        ans['bid'] = self.uid
        ans['about_id'] = self.about_id
        ans['name'] = self.name
        ans['release_time'] = self.release_time
        ans['update_time'] = self.update_time
        ans['all_catalog_count'] = self.node_sum
        ans['complete_count'] = self.complete_count
        ans['statistics'] = self.statistics.basic_info
        ans['keywords'] = self.keywords
        ans['islike'] = False if usr is None else usr.is_like(self)
        if info_name in ('basic_info'):
            ans['author'] = self.owner.obj_info_view_by(info_name, 
                            usr=usr, env=env, **kwargs)
        else:
            ans['author'] = self.owner.obj_info_view_by('overview_info',
                                    usr, env, **kwargs)
        ans['complete_rate'] = self.complete_rate
        if info_name == 'with_summary':
            ans['summary'] = self.about.obj_info_view_by('basic_info',
                            usr=usr, env=env, **kwargs)
        elif info_name == 'edit_with_summary':
            ans['summary'] = self.about.obj_info_view_by('edit_info',
                            usr=usr, env=env, **kwargs)
        else:
            ans['summary'] = None
        ans['chapter_list'] = self.node_list_info

        ans['permission'] = auth_str(self.authority_verify(
                    usr, env, **kwargs))
        return ans

    @db_property
    def as_env():
        def getter(self):
            ans = dict()
            ans['env_type'] = self.cls_name
            ans['env_id'] = self.uid
            ans['entity'] = self.as_env_info
            return ans
        return getter

    @db_property
    def as_env_info():
        def getter(self):
            ans = dict()
            ans['bid'] = self.uid
            ans['name'] = self.name
            ans['complete_rate'] = self.complete_rate
            ans['url'] = self.obj_url
            return ans
        return getter

    @db_property
    def obj_url():
        def getter(self):
            return self.main_url + 'book/' + self.uid
        return getter
