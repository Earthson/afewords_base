import markdown

DEL_RE = r'(--)(.+?)--'
INS_RE = r'(\.\.)(.+?)\.\.'

class InsDelExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        del_tag = markdown.inlinepatterns.SimpleTagPattern(DEL_RE, 'del')
        md.inlinePatterns.add('del', del_tag, '<not_strong')
        ins_tag = markdown.inlinepatterns.SimpleTagPattern(INS_RE, 'ins')
        md.inlinePatterns.add('ins', ins_tag, '<not_strong')

def makeExtension(configs=None):
    return InsDelExtension(configs)
