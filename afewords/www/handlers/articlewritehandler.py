#coding=utf-8
from basehandler import *
from pages.pages import WritePage

from authority import *
from afutils.type_utils import type_trans

class ArticleWritePara(BaseHandlerPara):
    paradoc = {
        'id': None,
        'type': 'blog',
        'env_type' : None,
        'env_id' : None,
    }

    def read(self):
        self['id'] = self.handler.get_esc_arg('id')
        self['type'] = self.handler.get_esc_arg('type', 'blog')
        self['env_type'] = self.handler.get_esc_arg('env_type', None)
        self['env_id'] = self.handler.get_esc_arg('env_id', None)


class ArticleWriteHandler(BaseHandler):
    
    @with_login
    def get(self):
        from generator import generator
        pageparas = ArticleWritePara(self)
        page = WritePage(self)
        usr = self.current_user
        page['article_type'] = pageparas['type']
        pageparas['env_type'] = type_trans(pageparas['env_type'])
        pageparas['type'] = type_trans(pageparas['type'])
        if not pageparas['type']:
            self.send_error(404, error_info=u'Invalid Article Type') #todo Earthson
            return
        if not pageparas['env_id'] and not pageparas['env_type']:
            page['owner'] = usr.as_env
            env_info = (usr._id, usr.__class__.__name__)
        else:
            env = generator(pageparas['env_id'], pageparas['env_type'])
            if not env:
                self.send_error(404, error_info=u'Invalid Envirenment')
                return
            env_info = (env.__class__.__name__, env._id)
            page['owner'] = env.as_env

        if not pageparas['id']:
            page.page_init()
            page.render()
            return
        page['isedit'] = True
        toedit = generator(pageparas['id'], pageparas['type'])
        if toedit is None:
            self.send_error(404, error_info=u'Article Not Found')
            return
        if (toedit.env_id, toedit.env_type) != env_info:
            self.send_error(404, error_info=u'Invalid Envirenment')
            return
        auth_ret = toedit.authority_verify(usr)
        if not test_auth(auth_ret, A_WRITE):
            self.send_error(404, error_info=u'Permission Denied')
            return
        page['article'] = toedit.edit_info
        page.page_init()
        page.render()
        return


class ArticleUpdatePara(BaseHandlerPara):
    paradoc = {
        'do': 'preview',    # unicode, preview or post
        'article_id': '-1', # unicode
        'article_type': 'blog', # unicode
        'title': '',    # unicode
        'body': '',     # unicode
        'summary': '',  # unicode
        'keywords': [], # list  self.get_arguments("keywords")
        'tags': [],     # list
        'env_id': '-1', # unicode
        'env_type': 'user', # unicode
        'privilege': 'public', # unicode
        
        #@comment
        'fahter_id': '-1',  # unicode
        'father_type': 'blog',  # unicode
        'ref_comments': [], # list
    }

    def read(self):
        self.paradoc = [(ek, self.handler.get_esc_arg(ek, ev)) 
                                    for ek, ev in self.paradoc]
        self['keywords'] = self.handler.get_esc_args('keywords[]')
        self['tags'] = self.handler.get_esc_args('tags[]')
        self['ref_comments'] = self.handler.get_esc_args('ref_comments[]')


from pages.postjson import UpdateArticlejson

class ArticleUpdateHandler(BaseHandler):

    @with_login
    def post(self)
        from generator import generator, cls_gen
        from article.article import Article
        handler_paras = ArticleUpdatePara(self)
        handler_json = UpdateArticleJson(self)
        usr = self.current_user
        env = generator(handler_paras['env_id'], 
                        type_trans(handler_paras['env_type']))
        if not env:
            handler_json.by_status(14)
            handler_json.write()
            return #Invalid Env Arguments
        if not Article.is_valid_id(handler_paras['article_id']):
            acls = cls_gen(trans_type(handler_paras['article_type']))
            if not acls:
                handler_json.by_status(11)
                handler_json.write()
                return #Invalid Article Type
            if not test_auth(env.authority_verify(usr), A_POST):
                handler_json.by_status(12)
                handler_json.write()
                return #Permission Denied
            article_obj = acls()
            article_obj.set_propertys(env=env, author=usr)
            if article_obj is None:
                handler_json.by_status(13)
                handler_json.write()
                return #Article Create Failed
            handler_json.as_new(article_obj.uid) 
            #new Article Created
        else:
            article_obj = genereator(handler_paras['article_id'],
                        type_trans(handler_paras['article_type']))
            if article_obj is None:
                handler_json.by_status(4)
                handler_json.write()
                return #Article Not Exist
            if article_obj.env_info != env.obj_info:
                handler_json.by_status(15)
                handler_json.write()
                return #Invalid Env
            if not test_auth(article_obj.authority_verify(usr, env),
                            A_WRITE):
                handler_json.by_status(16)
                handler_json.write()
                return #WRITE Permission Denied
        article_obj.set_by_info(handler_paras.load_doc())   
        author = article_obj.author
        if article_obj.is_posted is False:
            article_obj.tag = set(author.alltags) & \
                        set(handler_paras['tags'])
            if handler_paras['do'] == 'post':
                auth_ans = article_obj.authority_verify(usr, env)
                if not test_auth(auth_ans, A_POST):
                    handler_json.by_status(17)
                    handler_json.write()
                    return #Post Permission Denied
                author.post_article(article_obj) #try Post
        else:
            author.with_new_tags(article_obj, handler_paras['tags'])

        handler_json.by_status(0)
        handler_json.write()
        return #Return
