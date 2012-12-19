from markdown import Markdown

afmarkdown_settings = {
    'extensions' : [ #markdown extensions
        'insdel',
        'extra',
        'codehilite(force_linenos=True, css_class=highlight)',
        'mathjax',
    ],
    'output_format' : 'xhtml5',
    'safe_mode' : True,
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
