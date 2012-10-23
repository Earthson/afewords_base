from databox.afdocument import AFDocument
from databox.mongokit_utils import with_conn
from databox.databox import *

from translator.trans import reference_translator
from article_utils import is_url


@with_conn
class ReferenceDoc(AFDocument):
    __collection__ = 'ReferenceDB'

    structure = {
        'name' : basestring,
        'alias' : basestring,
        'body' : basestring,
        'body_version' : int,
        'view_body' : basestring,
        'view_body_version' : int,
        'url' : basestring,
    }
    required_fields = []
    default_values = {
        'name' : '',
        'alias' : '',
        'body' : '',
        'body_version' : 0,
        'view_body' : '',
        'view_body_version' : 0,
        'url' : '',
    }


@with_mapper
class Reference(DataBox):
    datatype = ReferenceDoc

    mapper = {
        'name' : True,
        'alias' : True,
        'url' : True,
    }

    translator = reference_translator

    def set_by_info(self, infodoc):
        ans = dict()
        ans['name'] = infodoc['title']
        ans['body'] = infodoc['body']
        ans['url'] = infodoc['source']
        self.set_propertys(**ans)

    @db_property
    def body():
        def getter(self):
            return self.data['body']
        def setter(self, value):
            self.data['body_version'] += 1
            self.data['body'] = value
        return getter, setter


    @db_property
    def view_body():
        def getter(self):
            if self.data['view_body_version'] == self.data['body_version']:
                return self.data['view_body']
            self.data['view_body_version'] = self.data['body_version']
            self.data['view_body'] = \
                    self.translator.translate(self.data['body'])
            ret = ''
            cbody = self.body
            name = self.name
            url = self.url
            if cbody is None or cbody == '':
                ret = r'<a href="%s" target="_blank" title="%s">' % (
                       url.replace('"', '%22'), name)
                ret += name + r'</a>'
            else:
                source = self.url
                if is_url(source):
                    source = r'<a href="%s" target="_blank" title="%s">' % (
                            source.replace('"', '%22'), name)
                    source += name + r'</a>'
                ss = self.data['view_body']
                ret = r'<div class="ref">'
                ret += r'<div class="ref-div">'
                ret += r'<div class="ref_open"></div>'
                ret += r'<div class="ref_close"></div>'
                ret += r'<div class="ref_source">[ %s ]</div>' % (
                        source)
                ret += r'<div class="ref_body">%s</div>' % ss
                ret += r'</div></div>'
            self.data['view_body'] = ret
            return self.data['view_body'], True
        return getter

    @db_property
    def basic_info():
        def getter(self):
            ans = dict()
            ans['alias'] = self.alias
            ans['name'] = self.name
            ans['url'] = self.url
            ans['body'] = self.body
            return ans
        return getter
