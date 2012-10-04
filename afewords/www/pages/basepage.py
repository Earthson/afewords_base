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

#@with_attr
class BasePage(object):
    __template__ = ''
    doc = {
        'title' : '', # the web page title
        'description' : '', # the web page description, maybe for SEO
        'user' : None, # the user's info, the value is returned by function user_to_dict
    }

    attr_template = {
        'user' : [
            'id', #unicode, user id
            'name', #unicode, user name
            'draft_count', #int, article num in drafts_lib
            'notice_count', #int, unread notification count
            'thumb_name', #unicode, user thumb
        ],
    }

    def __init__(self, handler, doc=None):
        self.handler = handler
        self.doc = dict(self.doc)
        if doc:
            self.doc.update(doc)

        #self.doc['user'] = user_to_dict(self.handler.current_user)
        self.doc['user'] = self.tmp_attr_gen(self.handler.current_user, 'user')

    def __getitem__(self, key):
        return self.doc[key]

    def __setitem__(self, key, value):
        return self.doc[key] = value

    def __delitem__(self, key):
        del self.doc[key]

    def render(self):
        return self.handler.render(self.__template__, doc=self.doc)

    show = render

    def render_string(self):
        return self.handler.render_string(self.__template__, doc=self.doc)

    __unicode__ = render_string
    __str__ = render_string

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


_tmp_tmp_ = '''
def user_to_dict(user):
    '''
    user info to dict:
        {
            '_id': 'a241212dsf', # unicode, user id
            'name': 'afewords', # unicode, user name
            'draft': '', # int, user draft's num
            'notice': '',  # int, user notification's num
            'thumb': '', # unicode, user thumb
            
        }
    '''
    if user is None:
        return None
    ret = dict()
    ret['_id'] = unicode(user._id)
    ret['name'] = user.name
    ret['thumb'] = user.avatar.tbumb_name
    ret['draft'] = len(user.draft_lib.load_all())
    ret['notice'] = len([i for i in user.notification_list.load_all() if i is not None and i[1] == False])
    return ret
'''
