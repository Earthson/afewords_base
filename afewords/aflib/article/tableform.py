from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *

import re

from translator import trans


@with_conn
class TableformDoc(AFDocument):
    __collection__ = 'TableformDB'

    structure = {
        'name' : basestring,
        'alias' : basestring,
        'tableform' : basestring,
    }
    required_fields = [] #['tableform']
    default_values = {
        'name' : '',
        'alias' : '',
    }


@with_mapper
class Tableform(DataBox):
    datatype = TableformDoc

    mapper = {
        'name' : True,
        'alias' : True,
        'tableform' : True,
    }

    normal_translator = trans.normal_translator

    def set_by_info(self, infodoc):
        ans = dict()
        ans['name'] = infodoc['title']
        ans['tableform'] = infodoc['body']
        self.set_propertys(**ans)

    @db_property
    def view_body():
        def getter(self):
            name = self.name
            ret = r'<div class="table">'
            ret += r'<div class="table_name">%s</div>' % name
            ret += r'<div><table><tbody>'
            lines = self.tableform
            lines = lines.splitlines()
            first = True
            mode = []
            for each in lines:
                if each.strip() == '':
                    continue
                ret += r'<tr>'
                tag = r'td'
                if first:
                    tag = r'th'
                tmp = each.split('||')
                for i in range(len(tmp)):
                    if len(mode) <= i:
                        mode.append('center')
                    mobj = re.search(r'#([r|l|c])$', tmp[i])
                    tmp[i] = re.sub(r'#[r|l|c]$', r'', tmp[i], 1)
                    tmp[i] = self.normal_translator.translate(tmp[i])
                    if mobj is not None:
                        if mobj.groups()[0] == 'r':
                            mode[i] = 'right'
                        elif mobj.groups()[0] == 'l':
                            mode[i] = 'left'
                        else:
                            mode[i] = 'center'
                    if first or mode[i] == 'center':
                        ret += r'<%s>%s</%s>' % (tag, tmp[i], tag)
                    else:
                        ret += r'<%s align="%s">%s</%s>' % (tag, mode[i],
                                                            tmp[i], tag)
                ret += r'</tr>'
                if first:
                    first = False
            ret += r'</tbody></table></div></div>'
            return ret
        return getter

    @db_property
    def basic_info():
        def getter(self):
            ans = dict()
            ans['alias'] = self.alias
            ans['name'] = self.name
            ans['body'] = self.tableform
            return ans
        return getter
