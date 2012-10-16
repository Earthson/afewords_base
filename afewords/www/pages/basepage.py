#coding=utf-8
from tornado.escape import json_encode
from tornado.template import Loader, Template
from afconfig import af_conf

def with_attr(cls):
    try:
        doc = dict(super(cls, cls).doc)
        doc.update(cls.doc)
        cls.doc = doc
        return cls
    except AttributeError:
        return cls

class AFDocBase(object):
    doc = {
        #name : defaut
    }

    def __init__(self, doc=None):
        self.doc = dict(self.doc)
        if doc:
            self.doc.update(doc)

    def __getitem__(self, key):
        return self.doc[key]

    def __setitem__(self, key, value):
        self.doc[key] = value

    def __delitem__(self, key):
        del self.doc[key]

    def __str__(self):
        return str(self.doc)

    def __unicode__(self):
        return unicode(self.doc)


@with_attr
class BaseToolPage(AFDocBase):
    __template_file__ = ''
    __loader__ = Loader('templates/tools')

    doc = {
        'main_url' : af_conf['main_url'],
    }

    def render_string(self):
        return self.__loader__.load(self.__template_file__).generate(doc=self.doc)

    __str__ = render_string


@with_attr
class BaseMail(AFDocBase):
    subject = u'Mail from afewords'
    __template_file__ = ''
    __loader__ = Loader('templates/mails')

    doc = {
        'main_url' : af_conf['main_url'],
    }
    
    def render_string(self):
        return self.__loader__.load(self.__template_file__).generate(doc=self.doc)
    
    __str__ = render_string
    #__unicode__ = render_string


@with_attr
class BaseJson(AFDocBase):

    def __init__(self, handler=None, doc=None):
        super(BaseJson, self).__init__(doc)
        self.handler = handler
    
    def write(self):
        self.handler.write(json_encode(self.doc))

    show = write
    
    def to_json(self):
        return json_encode(self.doc)


@with_attr
class BasePage(AFDocBase):
    __template_file__ = ''
    __loader__ = Loader('templates')
    doc = {
        'page_type' : 'index',  # web page type, for nav chosed
        'main_url' : af_conf['main_url'],
        'title' : '子曰', # the web page title
        'description' : '', # the web page description, maybe for SEO
        'user' : None, # the user's info, the value is returned by function user_to_dict
    }

    def __init__(self, handler=None, doc=None):
        super(BasePage, self).__init__(doc)
        self.handler = handler
        #self.doc['user'] = user_to_dict(self.handler.current_user)
        usr = self.handler.current_user
        if usr:
            self.doc['user'] = usr.notify_user_info

    def render(self):
        return self.handler.render(self.__template_file__, doc=self.doc)

    show = render

    def render_string(self):
        return self.__loader__.load(self.__template_file__).generate(doc=self.doc)

    #__unicode__ = render_string
    __str__ = render_string
