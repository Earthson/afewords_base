from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *

from datetime import datetime


@with_conn
class LangcodeDoc(AFDocument):
    __collection__ = 'LangcodeDB'

    structure = {
        'name' : basestring,
        'alias' : basestring,
        'lang' : basestring,
        'code' : basestring,
    }
    required_fields = ['code']
    default_values = {
        'name' : '',
        'alias' : '',
        'lang' : 'other',
    }


@with_mapper
class Langcode(DataBox):
    datatype = LangcodeDoc

    mapper = {
        'name' : True,
        'alias' : True,
        'lang' : True,
        'code' : True,
    }

    @db_property
    def view_body():
        def getter(self):
            bg = r'<div class="code">'
            bg += r'<div class="code-title">%s</div>' % self.name
            bg += r'<div><pre class="brush:%s;">' % self.lang + '\n'
            ed = '\n' + r'</pre></div>'
            ed += r'<div class="code-title">&nbsp;</div></div>'
            displaycode = self.code
            displaycode = displaycode.replace('<', '&lt;')
            displaycode = bg + displaycode + ed
            return displaycode
        return getter

