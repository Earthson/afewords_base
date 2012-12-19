from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter

class CodeHtmlFormatter(HtmlFormatter):
    def wrap(self, source, outfile):
        return self._wrap_code(source)

    def _wrap_code(self, source):
        yield 0, '<table class="highlight"><tbody>'
        cnt = 0
        for i, t in source:
            cnt += 1
            bg = '<tr class="line_%s">' % str(cnt%2)
            ss = '<td class="number"><code>' + str(cnt) + '</code></td>'
            ss += '<td class="content"><pre>' + t.split('\n')[0] + '</pre></td>'
            ed = '</tr>'
            yield i, bg+ss+ed
        yield 0, '</tbody></table>'


def code_parser(code, lang=None):
    try:
        if not lang:
            raise
        lexer = get_lexer_by_name("python", stripall=True)
    except:
        lexer = guess_lexer(code)
    formatter = CodeHtmlFormatter(cssclass="highlight")
    return highlight(code, lexer, formatter)


from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *

from datetime import datetime

from markup.parse import markup_parser


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

    as_reftype = u'code' #as_reftype should also in cls_alias

    def __init__(self, *args, **kwargs):
        DataBox.__init__(self, *args, **kwargs)
        self.parser = markup_parser('markdown')

    @class_property
    def cls_alias(cls):
        return u'code'

    def set_by_info(self, infodoc):
        ans = dict()
        ans['name'] = infodoc['title']
        ans['lang'] = infodoc['code_type']
        ans['code'] = infodoc['body']
        self.set_propertys(**ans)

    @db_property
    def view_body():
        def getter(self):
            '''
            bg = r'<div class="code">'
            bg += r'<div class="code-title">%s</div>' % self.name
            bg += r'<div><pre class="brush:%s;">' % self.lang + '\n'
            ed = '\n' + r'</pre></div>'
            ed += r'<div class="code-title">&nbsp;</div></div>'
            '''
            return code_parser(self.code, self.lang.lower())
            #bg = '\n\n'+r"````"+self.lang.lower()+'\n'
            #ed = "\n````\n\n"
            #displaycode = self.code
            #displaycode = displaycode.replace('<', '&lt;')
            #displaycode = bg + displaycode + ed
            #return self.parser(displaycode)
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
