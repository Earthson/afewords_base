#coding=utf-8
from tornado.escape import json_encode

def with_attr(cls):
    try:
        doc = super(cls, cls).doc
        doc.update(cls.doc)
        cls.doc = doc

        attr_template = super(cls, cls).attr_template
        attr_template.update(cls.attr_template)
        cls.attr_template = attr_template
        return cls
    except AttributeError:
        return cls

class AFDocBase(object):
    doc = {
        #name : defaut
    }

    attr_template = {
        #name : [namelist]
    }

    def __init__(self, handler, doc=None):
        self.handler = handler
        self.doc = dict(self.doc)
        if doc:
            self.doc.update(doc)

    @staticmethod
    def attr_gen(obj, *attrs):
        '''
        get attributes from obj by attrs, e.g.
        
        usr_dic = self.attr_gen(usrobj, *self.attr_template['user'])
        '''
        return dict(zip(attrs, obj.get_propertys(*attrs)))

    @classmethod
    def tmp_attr_gen(cls, obj, temp_name):
        return cls.attr_gen(obj, cls.attr_template[temp_name])

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
class BaseJson(AFDocBase):
    
    def write(self):
        self.handler.write(json_encode(self.doc))

    show = write
    
    def to_json(self):
        return json_encode(self.doc)


@with_attr
class BasePage(AFDocBase):
    __template_file__ = ''
    doc = {
        'title' : '子曰', # the web page title
        'description' : '', # the web page description, maybe for SEO
        'user' : None, # the user's info, the value is returned by function user_to_dict
    }

    attr_template = {
        'user' : [
            'uid', #unicode, user id
            'name', #unicode, user name
            'draft_count', #int, article num in drafts_lib
            'notice_count', #int, unread notification count
            'thumb_name', #unicode, user thumb
        ],
    }

    def __init__(self, handler, doc=None):
        super(BasePage, self).__init__(handler, doc)
        #self.doc['user'] = user_to_dict(self.handler.current_user)
        usr = self.handler.current_user
        if usr:
            self.doc['user'] = self.tmp_attr_gen(usr, 'user')

    def render(self):
        return self.handler.render(self.__template_file__, doc=self.doc)

    show = render

    def render_string(self):
        return self.handler.render_string(self.__template_file__, doc=self.doc)

    __unicode__ = render_string
    __str__ = render_string
