import re

class ReplacePattern(object):
    '''
    class for eeplace pattern in document
    prevent normal translation effects on text in these patterns
    
    __init__
    receive: pattern, re pattern for get text in doc
             repl, function to get text to replace the original text
                    repl receive a sub string of matched text(groups()[0])
    '''

    def __init__(self, pattern, repl):
        self.pattern = pattern
        self.repl = repl 


class RefPattern(object):
    '''
    similar to ReplacePattern, almost have the same interface
    you should not set pattern and repl(default one is good enough)
    you should pass a function that get text from tuple(reftype, refname)
    '''
    pattern = r'(?<!\\)\[([^:\]\s]+:[^:\]]+)(?<!\\)\]'
    def __init__(self, refinder):
        self.refinder = refinder

    def repl(self, mastr): 
        reftype, refname = mastr.split(':')
        return self.refinder(reftype, refname)

