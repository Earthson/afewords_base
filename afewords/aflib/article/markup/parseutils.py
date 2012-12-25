import re

import xml.etree.ElementTree as ET
from xml.sax.saxutils import unescape


def ref_parser(refinder=None):
    pattern = r'\[([a-zA-Z0-9]+:[a-zA-Z0-9]+)\]'
    pattern = re.compile(pattern)
    if refinder is None:
        refinder = lambda reftype, refname: '[%s:%s]' % (reftype, refname)
    def repl(mobj):
        reftype, refname = mobj.group(1).split(':')
        return '[fdksfdhfsdf]' + refinder(reftype, refname) + '[/fdksfdhfsdf]'
    return lambda txt:pattern.sub(repl, txt)


def fix_data():
    pattern = r'\[fdksfdhfsdf\]([\s\S]*?)\[/fdksfdhfsdf\]'
    pattern = re.compile(pattern)
    def repl(mobj):
        return unescape(mobj.group(1))
    return lambda txt: pattern.sub(repl, txt)

fix_data = fix_data()

def xml_parser(*parsers):
    def parse_all(txt):
        for each in parsers:
            txt = each(txt)
        return txt
    def parse_func(text):
        text = u'<div class="articlebody">' + text + u'</div>'
        #text = '<div>' + text + '</div>'
        etree = ET.fromstringlist(text.encode('utf-8'))
        def parse_node(node):
            if node.tag in ['code', 'mathjax', 'pre']:
                return
            if node.text:
                node.text = parse_all(node.text)
            for each in node:
                parse_node(each)
        for each in etree:
            parse_node(each)
        ans = ET.tostring(etree, encoding='utf-8', method="html")
        return fix_data(ans).decode('utf-8')#[5:-6]
    return parse_func
