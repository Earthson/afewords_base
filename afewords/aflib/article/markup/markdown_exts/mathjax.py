import markdown

_math_re = r'(?<!\\)(((\$\$?.+?(?<!\\)\$\$?)))'
#_equation_re = r'(?<!\\)(((\$\$[\s\S]+?(?<!\\)\$\$)))'

class MathJaxExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        # Needs to come before escape matching because \ is pretty important in LaTeX
        math_tag = markdown.inlinepatterns.SimpleTagPattern(_math_re, 'mathjax')
        md.inlinePatterns.add('mathjax', math_tag, '<escape')

def makeExtension(configs=None):
    return MathJaxExtension(configs)
