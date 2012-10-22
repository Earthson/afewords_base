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
    required_fields = [] #['code']
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

    def set_by_info(self, infodoc):
        ans = dict()
        ans['name'] = infodoc['title']
        ans['lang'] = infodoc['code_type']
        ans['code'] = infodoc['body']
        self.set_propertys(**ans)

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

    @db_property
    def basic_info():
        def getter(self):
            ans = dict()
            ans['alias'] = self.alias
            ans['name'] = self.name
            ans['lang'] = self.lang
            ans['body'] = self.code
            return ans
        return getter
