import re
from replacepattern import ReplacePattern, RefPattern


class Translator(object):
    '''Document Translator'''
    def __init__(self, protect_trans, line_trans):
        self.protect_trans = protect_trans
        self.line_trans = line_trans

    def translate(self, idoc):
        idoc = idoc.replace(r'<', r'&lt;')
        idoc, plist = self.protect_trans.translate(idoc)
    
        lines = split_to_lines(idoc) #split and do list translate
        
        for i in range(len(lines)):
            lines[i] = self.line_trans.translate(lines[i])
        idoc = merge_lines(lines)   
        idoc = self.protect_trans.restore(idoc, plist)
        return idoc
        

protect_bg = r'prot'
protect_ed = r'torp'
protect_pattern = re.compile(protect_bg + r'([0-9]*?)' + protect_ed)

def _pbg_repl(mastr):
    return mastr

def _ped_repl(mastr):
    return mastr

_ipbg = ReplacePattern('(' + protect_bg + ')', _pbg_repl)
_iped = ReplacePattern('(' + protect_ed + ')', _ped_repl)


class ProtectTranslator(object):
    '''
    object to do protect translate
    you should add your replace patterns to self.replacelist
    if you change the allpattern after init, 
        you should do self.compile method to do some init
    then self.translate is availabe
    '''
    replacelist = []

    allpattern = None 
    allrepl = []

    def __init__(self, *replacelist):
        self.replacelist = [_ipbg, _iped]
        self.replacelist += replacelist
        self.compile()

    def compile(self): 
        tmp = '|'.join(each.pattern for each in self.replacelist)
        self.allpattern = re.compile(tmp)
        self.allrepl = [each.repl for each in self.replacelist]

    def translate(self, idoc):
        '''return (idoc, replist)'''
        replist = list()
        cnt = [0]
        if self.allpattern is None:
            return (idoc, ['please compile the translator first'])
        
        def arepl(mobj):
            gg = mobj.groups()
            for i in range(len(gg)):
                if gg[i] is None:
                    continue
                #print self.allrepl[i](gg[i])
                replist.append(self.allrepl[i](gg[i]))
                ret = protect_bg + str(cnt[0]) + protect_ed
                cnt[0] += 1
                return ret
            
        idoc = self.allpattern.sub(arepl, idoc)
        return (idoc, replist)

    def restore(self, idoc, replist):
        '''replace with string in replist'''
        
        def brepl(mobj):
            return replist[int(mobj.groups()[0])]

        return protect_pattern.sub(brepl, idoc)





class LineTranslator(object):
    '''translator for line
       you need add some replace patterns by your self
    '''
    replacelist = []
    allpattern = None
    allrepl = []
    
    def __init__(self, *replpatterns):
        self.replacelist = replpatterns
        self.compile()

    def compile(self):
        tmp = '|'.join(each.pattern for each in self.replacelist)
        self.allpattern = re.compile(tmp)
        self.allrepl = [each.repl for each in self.replacelist]

    def translate(self, line):
        
        def arepl(mobj):
            gg = mobj.groups()
            for i in range(len(gg)):
                if gg[i] is None:
                    continue
                return self.translate(self.allrepl[i](gg[i]))

        return self.allpattern.sub(arepl, line)




def split_to_lines(idoc):
    lines = idoc.splitlines()
    return dolist_translate(lines)


def merge_lines(lines):
    #brstr = r'<div class="br"></div>'
    #return '\n'.join(r'<div>' + each + r'</div>' if each != brstr else each
    #                     for each in lines)
    return '\n'.join(lines)


def dolist_translate(lines):
    '''translation for <ul><ol><li>'''
    lcnt = len(lines)
    curline = 0
    tolist = []
    while curline < lcnt:
        if lines[curline] == '':
            tolist.append('')
            curline += 1
        elif lines[curline][0] == '*':
            ss, curline = list_trans(lines, curline, '*', '*')
            tolist.append(ss)
        elif lines[curline][0] == '#':
            ss, curline = list_trans(lines, curline, '#', '#')
            tolist.append(ss)
        else:
            tolist.append(lines[curline])
            curline += 1
    return tolist


def has_prefix(tomatch, pre):
    '''judge tomatch wheather have prefix pre'''
    slen = len(pre)
    if tomatch[0:slen] == pre[0:slen]:
        return True
    return False


def list_trans(lines, curline, flag, prefix = ''):
    '''sub function for translation for <ul> <ol> <li>'''
    lcnt = len(lines)
    mlen = len(prefix)
    res, end = None, None
    if flag == '*':
        #res, end = '<ul>', '</ul>'
        res, end = '', ''
    else:
        #res, end = '<ol>', '</ol>'
        res, end = '', ''
    while curline < lcnt:
        if has_prefix(lines[curline], prefix + '*'):
            ss, curline = list_trans(lines, curline, '*', prefix + '*')
            res += ss
        elif has_prefix(lines[curline], prefix + '#'):
            ss, curline = list_trans(lines, curline, '#', prefix + '#')
            res += ss
        elif has_prefix(lines[curline], prefix):
            tmp = prefix[-1]
            if tmp == '#':
                tmp = '1.  '
            else:
                tmp = '*   '
            tmp = ''.join(['    ' for each in prefix[:-1]]) + tmp
            res += tmp + lines[curline][mlen:] + '\n'#+ '</li>'
            #res += '<li>' + lines[curline][mlen:] + '</li>\n'
            curline += 1
        else:
            res += end
            return (res, curline)
    res += end
    return (res, curline)
