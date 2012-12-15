from afmarkdown import afmarkdown
from parseutils import ref_parser

def article_parser(refinder=None, lang='markdown'):
    if lang == 'markdown':
        markup_parser = afmarkdown()
    afref_parser = ref_parser(refinder)
    def parser(txt):
        txt = markup_parser(txt)
        txt = afref_parser(txt)
        return txt
    return parser
