from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *
from emmongodict.emmongodict import EmMongoDict

from bson import ObjectId
from datetime import datetime

from statistics import Statistics
from about import About
from generator import *
from utils.relation import Relation


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
        #todo Earthson
        return ans

    @property
    def parent_catalogs(self):
        return self.sub_dict('parent_catalogs',
                    generator=id_generator(Catalog))

    @property
    def feedback_list(self):
        from feedback import Feedback
        return self.sub_list('feedback_list',
                    generator=id_generator(Feedback))

    @property
    def topic_list(self):
        from topic import Topic
        return self.sub_list('topic_list',
                    generator=id_generator(Topic))

    @property
    def node_lib(self):
        return self.sub_dict('node_lib')

    @property
    def node_info_lib(self):
        return self.sub_dict('node_info_lib')

    @property
    def relations_list(self):
        return self.sub_list('relations_list',
                    generator=id_generator(Relation))


@with_conn
class CatalogDoc(AFDocument):
    __collection__ = 'CatalogDB'

    structure = {
        'name' : basestring,
        'owner_id' : basestring,
        'owner_type' : basestring,
        'managers' : [ObjectId], #User id
        'node_count' : int,
        'remove_count' : int,
        'complete_count' : int,
        'release_time' : datetime,
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
        'about_id' : About.new_doc,
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
    }
    own_data = ['statistics', 'about', 'lib']

    @db_property
    def statistics():
        def getter(self):
            return id_generator(Statistics)(self.data['statistics_id'])
        return getter

    @db_property
    def about():
        '''introduction page to user'''
        def getter(self):
            return id_generator(About)(self.data['about_id'])
        return getter

    @db_property
    def lib():
        def getter(self):
            return CatalogLib(spec={'_id':self.data['lib_id']})
        return getter

    @db_property
    def owner():
        def getter(self):
            return generator(self.data['owner_type'], self.data['owner_id'])
        def setter(self, value):
            self.data['owner_type'] = value.__class__.__name__
            self.data['owner_id'] = value._id
        return getter, setter

    @db_property
    def node_sum():
        def getter(self):
            return self.data['node_count'] - self.data['remove_count']
        return getter

    def authority_verify(self, usr, **env):
        ret = 0
        if usr == None:
            ret = set_auth(ret, A_READ)
        elif self.owner_type == usr.__class__.__name__ and \
                str(self.owner_id) == str(usr._id):
            ret = set_auth(ret, A_READ | A_WRITE | A_MANAGE | A_DEL)
        elif usr._id in set(self.managers):
            ret = set_auth(ret, A_READ | A_WRITE | A_MANAGE)
        ret |= BaseClass.authority_verify(self, usr, **env)
        return ret

    def spec_blog_to(self, node_id, rel_obj):
        tmp = self.get_node_list(node_id, 'main')
        tmp_all = tmp.load_all()
        if rel_obj._id in tmp_all:
            return None
        if len(tmp) == 0:
            self.complete_count += 1
        tmp.push(rel_obj._id)
        self.get_node_dict(node_id)['spec_count'] += 1

    def unspec_blog_to(self, node_id, rel_obj):
        tmp = self.get_node_list(node_id, 'main')
        tmpset = set(tmp.load_all())
        if rel_obj._id in tmpset:
            tmpset.discard(rel_obj._id)
            if len(tmpset) == 0:
                self.complete_count -= 1
            tmp.set_list(list(tmpset))
            self.get_node_dict(node_id)['spec_count'] -= 1

    def recommend_article(self, node_id, article_obj):
        rr = Relation(attrs={"relation_type":"catalog-%s" % \
                            article_obj.__class__.__name__})
        rr.set_relation_set(self, article_obj)
        tmp = self.get_node_list(node_id, 'articles')
        tmp.push(rr._id)
        self.lib.relations_list.push(rr._id)
        self.get_node_dict(node_id)['article_count'] += 1
        return rr

    def remove_article(self, node_id, rel_obj):
        self.lib.relations_list.pull(rel_obj._id)
        self.get_node_list(node_id, 'articles').pull(rel_obj._id)
        self.unspec_blog_to(node_id, rel_obj)
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
            'main':list(),
            'articles':list(),
            'catalogs':list(),
        }
        self.node_lib[str(self.node_count)] = tmp_node
        self.node_info_lib[str(self.node_count)] = tmp_info
        self.node_count += 1
        return self.node_count - 1

    def remove_node(self, node_id):
        tmp_rel_ids = self.get_node_list(node_id, 'articles').load_all()
        self.lib.relations_list.pull(*tuple(tmp_rel_ids))
        rels = Relation.get_instances('_id',
                self.get_node_list(node_id, 'articles').load_all())
        for each in rels:
            each.remove()
        tmp_rel_ids = self.get_node_list(node_id, 'catalogs').load_all()
        self.lib.relations_list.pull(*tuple(tmp_rel_ids))
        self.remove_count += 1
        if self.get_node_list(node_id, 'main').load_all() != []:
            self.complete_count -= 1
        rels = Relation.get_instances('_id',
                self.get_node_list(node_id, 'catalogs').load_all())
        for each in rels:
            each.remove()
        del self.lib.node_lib[node_id]
        del self.lib.node_info_lib[node_id]

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

    #property for page&json
    @db_property
    def basic_info():
        def getter(self):
            ans = dict()
            ans['bid'] = self.uid
            ans['name'] = self.name
            ans['all_count'] = self.node_sum
            ans['complete_count'] = self.complete_count
            ans['author'] = self.owner.basic_info
            return getter
        return getter
