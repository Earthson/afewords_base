from markdown import Markdown

afmarkdown_settings = {
    'extensions' : [ #markdown extensions
        'extra',
        'codehilite',
    ],
    'output_format' : 'xhtml5',
}


class AFMarkdown(Markdown):
    '''afewords style markdown configuration'''
    ESCAPED_CHARS = Markdown.ESCAPED_CHARS + ['$']


def afmarkdown(settings=afmarkdown_settings):
    newpaser = AFMarkdown(**settings)
    def paser(txt):
        newpaser.reset()
        return newpaser.convert(txt)
    return paser
