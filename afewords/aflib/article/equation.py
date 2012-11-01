from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *


@with_conn
class EquationDoc(AFDocument):
    __collection__ = 'EquationDB'

    structure = {
        'name' : basestring,
        'alias' : basestring,
        'mode' : basestring,
        'equation' : basestring,
    }
    required_fields = [] #['equation']
    default_values = {
        'name' : '',
        'alias' : '',
        'mode' : 'display', # inline/display
    }


@with_mapper
class Equation(DataBox):
    datatype = EquationDoc

    mapper = {
        'name' : True,
        'alias' : True,
        'mode' : True,
        'equation' : True,
    }

    as_reftype = u'math' #as_reftype should also in cls_alias

    @class_property
    def cls_alias(cls):
        return u'math'

    def set_by_info(self, infodoc):
        ans = dict()
        ans['name'] = infodoc['title']
        ans['mode'] = infodoc['math_mode']
        if ans['mode'] not in ['display', 'inline']:
            ans['mode'] = 'display'
        ans['equation'] = infodoc['body']
        self.set_propertys(**ans)

    @db_property
    def view_body():
        def getter(self):
            ret = '<div class="math">'
            ret += '[math]' if self.mode == 'inline' else '[equation]'
            ret += self.equation
            ret += '[/math]\n</div>' if self.mode == 'inline' else \
                        '[/equation]\n</div>'
            return ret
        return getter


    @db_property
    def basic_info():
        def getter(self):
            ans = dict()
            ans['alias'] = self.alias
            ans['name'] = self.name
            ans['mode'] = self.mode
            ans['body'] = self.equation
            return ans
        return getter
