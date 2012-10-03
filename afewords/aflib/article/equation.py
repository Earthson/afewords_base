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
    required_fields = ['equation']
    default_values = {
        'name' : '',
        'alias' : '',
        'mode' : 'display',
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

