#coding=utf-8
from basehandler import *
from pages.pages import WritePage

from authority import *
from afutils.type_utils import type_trans

from generator import generator, cls_gen
from article.article import Article

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


def article_env_init(handler, handler_paras, handler_json):
    handler_json['article_id'] = handler_paras['article_id']
    usr = handler.current_user
    env = generator(handler_paras['env_id'], handler_paras['env_type'])
    handler.env = env #Store env obj
    if not env:
        return 14#Invalid Env Arguments
    father = generator(handler_paras['father_id'], 
                type_trans(handler_paras['father_type']))
    ref_comment = None
    if handler_paras['article_type'] == 'comment':
        if father is None:
            return 18#Invalid father
        ref_comment = generator(handler_paras['ref_comment'], 
                            type_trans(handler_paras['article_type']))
    if not Article.is_valid_id(handler_paras['article_id']):
        acls = cls_gen(type_trans(handler_paras['article_type']))
        if not acls:
            return 11#Invalid Article Type
        if not test_auth(env.authority_verify(usr), A_POST):
            return 12#Permission Denied
        handler.article_obj = acls()
        handler.article_obj.set_propertys(env=env, author=usr)
        usr.add_to_drafts(handler.article_obj)
        if handler.article_obj is None:
            return 13#Article Create Failed
        handler_json.as_new(handler.article_obj.uid) 
        #new Article Created
    else:
        handler.article_obj = generator(handler_paras['article_id'],
                    type_trans(handler_paras['article_type']))
        if handler.article_obj is None:
            return 4#Article Not Exist
        if handler.article_obj.env_obj_info != env.obj_info:
            return 15#Invalid Env
        if not test_auth(handler.article_obj.authority_verify(usr, env),
                        A_WRITE):
            return 16#WRITE Permission Denied
    handler.father = None
    handler.ref_comment = None
    if father is not None:
        handler.father = father
        handler.article_obj.father = father
    if ref_comment is not None:
        handler.ref_comment = ref_comment
        handler.article_obj.ref_comment = ref_comment
    return 0

class BaseArticleUpdateHandler(BaseHandler):
    env_init = article_env_init


class ArticleUpdatePara(BaseHandlerPara):
    paradoc = {
        'do': 'update',    # unicode, update or post
        'article_id': '-1', # unicode
        'article_type': 'blog', # unicode
        'title': '',    # unicode
        'body': '',     # unicode
        'summary': '',  # unicode
        'keywords': '', # list  self.get_arguments("keywords")
        'tags': [],     # list
        'env_id': '-1', # unicode
        'env_type': 'user', # unicode
        'privilege': 'public', # unicode
        
        #@comment
        'father_id': '-1',  # unicode
        'father_type': 'blog',  # unicode
        'ref_comment': None, # list
    }

    def read(self):
        self.paradoc = dict([(ek, self.handler.get_esc_arg(ek, ev)) 
                                    for ek, ev in self.paradoc.items()])
        self['tags'] = self.handler.get_esc_args('tags[]')
        self['ref_comments'] = self.handler.get_esc_args('ref_comments[]')
        self['tags'].append('default')
        self['keywords'] = self['keywords'].replace(u'，', u',').split(u',')
        if self['privilege'] not in ['public', 'private']:
            self['privilege'] = 'public'
    

from pages.postjson import UpdateArticleJson
from pages.messages import BeCommentedMSG

class ArticleUpdateHandler(BaseArticleUpdateHandler):

    @with_login_post
    def post(self):
        handler_paras = ArticleUpdatePara(self)
        handler_json = UpdateArticleJson(self)
        usr = self.current_user
        status = self.env_init(handler_paras, handler_json)
        if status != 0:
            handler_json.by_status(status)
            handler_json.write()
            return #Error
        #try article update
        self.article_obj.set_by_info(handler_paras.load_doc())    
        author = self.article_obj.author
        if self.article_obj.is_posted is False:
            if handler_paras['article_type'] not in ['comment']:
                self.article_obj.tag = list(set(author.alltags) & 
                        set(handler_paras['tags']))
            if handler_paras['do'] == 'post':
                auth_ans = self.article_obj.authority_verify(usr, self.env)
                if not test_auth(auth_ans, A_POST):
                    handler_json.by_status(17)
                    handler_json.write()
                    return #Post Permission Denied
                author.post_article(self.article_obj.obj_info[1], 
                                self.article_obj) #try Post
                if handler_paras['article_type'] in ['comment']:
                    msg = BeCommentedMSG()
                    msg.comment_by(self.father, self.article_obj)
                    msg_str = msg.render_string()
                    father_author = self.father.author
                    father_author.accept_notification(msg_str, usr)
                    if self.ref_comment:
                        ref_comment_author = self.ref_comment.author
                        if father_author != ref_comment_author:
                            ref_comment_author.accept_notification(msg_str, usr)
        elif handler_paras['article_type'] not in ['comment']:
            author.with_new_tags(self.article_obj, handler_paras['tags'])

        handler_json['article_id'] = self.article_obj.uid
        handler_json.by_status(0)
        handler_json.write()
        return #Return


from afutils.img_utils import upload_img

class ArticleSrcPara(BaseHandlerPara):
    paradoc = {
        'do': 'new',    # unicode, new/edit/remove
        'article_id': '',   # unicode
        'article_type': 'blog', # unicode
        'env_id': '',   # unicode
        'env_type': 'user', # unicode
        'father_id': '',    # unicode
        'father_type': 'blog',  # unicode
        'src_type': 'math', # unicode, math/code/table/ref/img
        'src_alias': '',   # unicode, alias
        'title': '',    # unicode
        'body': '', # unicode
        
        #@for reference
        'source': '',  # unicode
        #@for langcode
        'code_type': 'python',  # unicode
        #@for equation
        'math_mode': 'display', # unicode
        #@for picture
        'picture' : None, #handler.requeset.files['picture']
    }

    src_types = ['img', 'math', 'code', 'table', 'ref']

    def read(self):
        self.paradoc = dict([(ek, self.handler.get_esc_arg(ek, ev)) 
                                    for ek, ev in self.paradoc.items()])
        self.error_code = 0
        if self.paradoc['src_type'] != 'img':
            return
        try:
            self.paradoc['picture'] = self.handler.request.files['picture'][0]
        except KeyError, e:
            self.paradoc['picture'] = None
        if self.paradoc['picture']:
            status, info = upload_img(self.paradoc['picture'])
            if status == 0:
                self.paradoc['picture'] = info
            self.error_code = status
        elif self.paradoc['do'] == 'new':
            self.error_code = 55

from pages.postjson import ArticleSrcJson

class ArticleSrcHandler(BaseArticleUpdateHandler):
    '''for article lib: picture langcode math and etc.'''
    @with_login_post
    def post(self):
        handler_paras = ArticleSrcPara(self)
        handler_json = ArticleSrcJson(self)
        usr = self.current_user
        status = self.env_init(handler_paras, handler_json)
        handler_json['src_alias'] = handler_paras['src_alias']
        if status == 0 and handler_paras.error_code > 0:
            #data read error
            status = handler_paras.error_code
        if status != 0:
            handler_json.by_status(status)
            handler_json.write()
            return #Error
        if handler_paras['do'] not in ['new', 'edit', 'remove']:
            handler_json.by_status(8)
            handler_json.write()
            return #Unsupported Operation
        if handler_paras['src_type'] not in handler_paras.src_types:
            handler_json.by_status(5)
            handler_json.write()
            return #Unsupported Ref Type
        if handler_paras['do'] == 'new':
            scls = cls_gen(type_trans(handler_paras['src_type']))
            if scls is None:
                handler_json.by_status(5)
                handler_json.write()
                return #Unsupported Ref Type
            src_obj = scls()
            self.article_obj.add_ref(handler_paras['src_type'], src_obj)
            handler_json.as_new_src(src_obj)
            src_obj.set_by_info(handler_paras.load_doc())
            if handler_paras['src_type'] == 'img':
                handler_json['img_url'] = src_obj.thumb_url
            handler_json.by_status(0)
            handler_json.write()
            return #0
        elif handler_paras['do'] == 'remove':
            self.article_obj.remove_ref(handler_paras['src_type'],
                                handler_paras['src_alias'])
            handler_json.by_status(0)
            handler_json.write()
            return #0
        elif handler_paras['do'] == 'edit':
            src_obj = self.article_obj.get_ref(handler_paras['src_type'],
                                handler_paras['src_alias']) 
            if src_obj is None:
                handler_json.by_status(18)
                handler_json.write()
                return #Src Not Exist
            src_obj.set_by_info(handler_paras.load_doc())
            if handler_paras['src_type'] == 'img':
                handler_json['img_url'] = src_obj.thumb_url
            self.article_obj.do_update()
            handler_json.by_status(0)
            handler_json.write()
            return #0
        handler_json.by_status(8)
        handler.write()
        return #Unexpected Operation
