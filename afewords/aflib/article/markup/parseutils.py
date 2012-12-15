import re

def ref_parser(refinder=None):
    pattern = r'(?<!\\)\[([a-zA-Z0-9]+:[a-zA-Z0-9]+)\]'
    pattern = re.compile(pattern)
    if refinder is None:
        refinder = lambda reftype, refname: '[%s:%s]' % (reftype, refname)
    def repl(mobj):
        reftype, refname = mobj.groups()[0].split(':')
        return refinder(reftype, refname)
    return lambda txt:pattern.sub(repl, txt)
