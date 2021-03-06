#coding=utf-8
import os
from tornado.escape import json_encode, xhtml_unescape
from tornado.template import Loader, Template
from afconfig import af_conf
from datetime import datetime

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

    def update(self, **doc):
        for ek, ev in doc.items():
            self.doc[ek] = ev

    def __str__(self):
        return str(self.doc)

    def __unicode__(self):
        return unicode(self.doc)


import PyRSS2Gen

class BaseRSSPage(AFDocBase):
    doc = {
        'title' : u'',
        'link' : u'',
        'description' : u'',
        'lastBuildDate' : datetime.now(),
        'items' : [],
    }

    def __init__(self, handler=None, doc=None):
        super(BaseRSSPage, self).__init__(doc)
        self.handler = handler

    def init_page(self):
        '''init after items is set'''
        self['items'] = [PyRSS2Gen.RSSItem(**each) for each in self['items']]

    def render_string(self):
        rss = PyRSS2Gen.RSS2(**self.doc)
        return rss.to_xml(encoding="utf-8")

    def render(self):
        return self.handler.write(self.render_string())


from pyatom import AtomFeed, FeedEntry

class BaseAtomPage(AFDocBase):
    doc = {
        'title':u'',
        'subtitle':u'',
        'feed_url':'',
        'url':'',
        'author':'',
        'entries':[],
    }

    def __init__(self, handler=None, doc=None):
        super(BaseAtomPage, self).__init__(doc)
        self.handler = handler

    def render_string(self):
        feed = AtomFeed(**self.doc)
        return feed.to_string()

    def render(self):
        return self.handler.write(self.render_string())

    def init_page(self):
        self['entries'] = [FeedEntry(**each) for each in self['entries']]

    def add_entries(self, *entries):
        self['entries'].extend(entries) 


@with_attr
class BaseToolPage(AFDocBase):
    __template_file__ = ''
    __loader__ = Loader(os.path.join(af_conf['root_dir'], 'templates/tools'))

    doc = {
        'main_url' : af_conf['main_url'],
    }

    def render_string(self):
        return self.__loader__.load(self.__template_file__).generate(doc=self.doc)

    __str__ = render_string


@with_attr
class BaseStringRender(AFDocBase):
    __template_file__ = ''
    __loader__ = Loader(os.path.join(af_conf['root_dir'], 'templates'))

    doc = {
        'main_url' : af_conf['main_url'],
    }

    
    def render_string(self):
        return self.__loader__.load(self.__template_file__).generate(doc=self.doc)
    
    __str__ = render_string
    #__unicode__ = render_string


@with_attr
class BaseMail(BaseStringRender):
    subject = u'Mail from afewords'
    __loader__ = Loader(os.path.join(af_conf['root_dir'], 'templates/mails'))


@with_attr
class BaseMSG(BaseStringRender):
    subject = u'Mail from afewords'
    __loader__ = Loader(os.path.join(af_conf['root_dir'], 'templates/messages'))


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
    __loader__ = Loader(os.path.join(af_conf['root_dir'], 'templates'))
    doc = {
        'page_type' : 'index',  # web page type, for nav chosed
        'subpage_type' : 'feed',
        'main_url' : af_conf['main_url'],
        'title' : '子曰', # the web page title
        'description' : '子曰博客和知识谱为你提供开源的环境', # the web page description, maybe for SEO
        'meta_keywords': ['子曰', '子曰博客', '子曰知识谱'],    # for SEO
        'user' : None, # the user's info, the value is returned by function user_to_dict
    }

    def __init__(self, handler=None, doc=None):
        super(BasePage, self).__init__(doc)
        self.handler = handler
        usr = self.handler.current_user
        if usr:
            self.doc['user'] = usr.notify_user_info

    def render(self):
        return self.handler.render(self.__template_file__, doc=self.doc, 
                        xhtml_unescape=xhtml_unescape)

    show = render

    def render_string(self):
        if self.handler is not None:
            return self.handler.render_string(self.__template_file__, 
                        doc=self.doc, xhtml_unescape=xhtml_unescape)
        return self.__loader__.load(self.__template_file__).generate(doc=self.doc, xhtml_unescape=xhtml_unescape)

    #__unicode__ = render_string
    __str__ = render_string
