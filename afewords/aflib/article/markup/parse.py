from afmarkdown import afmarkdown
from parseutils import ref_parser

def article_parser(refinder=None, lang='markdown'):
    if lang == 'markdown':
        markup_parser = afmarkdown()
    else:
        raise KeyError()
    afref_parser = ref_parser(refinder)
    def parser(txt):
        txt = markup_parser(txt)
        txt = afref_parser(txt)
        return txt
    return parser

def markup_parser(lang='markdown'):
    if lang == 'markdown':
        m_parser = afmarkdown()
    else:
        raise KeyError()
    return lambda txt: m_parser(txt)
