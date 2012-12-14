import re
from replacepattern import ReplacePattern

'''
definations of some protect pattern

before escape
types: iurl, imath, iequation 

escape
type: iesc
'''

def get_inline_ref_pattern(name):
    '''you can get inline reference pattern using this function'''
    name = re.escape(name)
    return r'(?<!\\)\[%s\]([\s\S]+?)\[/%s\]' % (name, name)

_ilink_pattern = get_inline_ref_pattern('link')

def _ilink_repl(mastr):
    tmp = mastr.split('---', 1)
    if len(tmp) == 2:
        name, url = mastr.split('---', 1)
    else:
        name = url = tmp[0]
    return ur'[%s](%s)' % (name, url)
    #return r'<a href="%s" target="_blank" title="%s">%s</a>' % (
            #url.replace('"', '%22'), name, name)

ilink = ReplacePattern(_ilink_pattern, _ilink_repl)

_icode_pattern = get_inline_ref_pattern('code')

def _icode_repl(mastr):
    return '<code>'+mastr+'</code>'
    #return ur'<div><pre class="afewords-brush">' + mastr + ur'</pre></div>'

icode = ReplacePattern(_icode_pattern, _icode_repl)

#in line url
_iurl_pattern = r'(\b(?:http|ftp|https)://(?:.*?)(?:(?=\s)|$))'
def _iurl_repl(mastr):
    return r'<a href="%s" target="_blank">%s</a>' % (
            mastr.replace('"', '%22'), mastr)

#iurl = ReplacePattern(_iurl_pattern, _iurl_repl)

#in doc math
_imath_pattern = get_inline_ref_pattern('math')
def _imath_repl(mastr):
    ret = r'<div class="math">'
    #ret += r'[math]'
    #ret += mastr + r'[/math]</div>'
    ret += r'$'
    ret += mastr + r'$</div>'
    return ret

imath = ReplacePattern(_imath_pattern, _imath_repl)

#in doc equation
_iequation_pattern = get_inline_ref_pattern('equation')
def _iequation_repl(mastr):
    ret = r'<div class="math">'
    #ret += r'[equation]'
    ret += r'$$'
    #ret += mastr + r'[/equation]</div>'
    ret += mastr + r'$$</div>'
    return ret

iequation = ReplacePattern(_iequation_pattern, _iequation_repl)

#escape
ecslist = r'''\[]+-_/^=*#}{$()'''
_iesc_pattern = '('+'|'.join([re.escape('\\' + each) for each in ecslist])+')'
def _iesc_repl(mastr):
    return mastr[1]

iesc = ReplacePattern(_iesc_pattern, _iesc_repl)




#h2
_ih2_pattern = r'==([^=].*?)=='
def _ih2_repl(mastr):
    #return r'<h2>' + mastr + r'</h2>'
    return r'## ' + mastr + ' ##'

ih2 = ReplacePattern(_ih2_pattern, _ih2_repl)

#h3
_ih3_pattern = r'===([^=].*?)==='
def _ih3_repl(mastr):
    #return r'<h3>' + mastr + r'</h3>'
    return r'### ' + mastr + r' ###'

ih3 = ReplacePattern(_ih3_pattern, _ih3_repl)

#h4
_ih4_pattern = r'====([^=].*?)===='
def _ih4_repl(mastr):
    #return r'<h4>' + mastr + r'</h4>'
    return r'#### ' + mastr + r' ####'

ih4 = ReplacePattern(_ih4_pattern, _ih4_repl)

#Bold
_ibold_pattern = r'\+\+([^\+].*?)\+\+'
def _ibold_repl(mastr):
    #return r'<b>' + mastr + r'</b>'
    return r'**' + mastr + '**'

ibold = ReplacePattern(_ibold_pattern, _ibold_repl)

#del
_idel_pattern = r'--([^-].*?)--'
def _idel_repl(mastr):
    return r'<del>' + mastr + r'</del>'

idel = ReplacePattern(_idel_pattern, _idel_repl)

#ins
_iins_pattern = r'__([^_].*?)__'
def _iins_repl(mastr):
    return r'<ins>' + mastr + r'</ins>'

iins = ReplacePattern(_iins_pattern, _iins_repl)

#italic
_iitalic_pattern = r'//([^/].*?)//'
def _iitalic_repl(mastr):
    return r'*' + mastr + r'*'
    #return r'<i>' + mastr + r'</i>'

iitalic = ReplacePattern(_iitalic_pattern, _iitalic_repl)

#sup
_isup_pattern = r'\^\{(.*?)\}'
def _isup_repl(mastr):
    return r'<sup>' + mastr + r'</sup>'

isup = ReplacePattern(_isup_pattern, _isup_repl)

#sub
_isub_pattern = r'_\{(.*?)\}'
def _isub_repl(mastr):
    return r'<sub>' + mastr + r'</sub>'

isub = ReplacePattern(_isub_pattern, _isub_repl)

#ibr
_ibr_pattern = r'^()$'
def _ibr_repl(mastr):
    #return r'<div class="br"></div>'
    return '\n\n'

ibr = ReplacePattern(_ibr_pattern, _ibr_repl)

#ihr
_ihr_pattern = r'^(~+)$'
def _ihr_repl(mastr):
    #return r'<div class="hr"></div>'
    return r'- - -'

ihr = ReplacePattern(_ihr_pattern, _ihr_repl)

#iindent
_iindent3_pattern = r'^&gt;&gt;&gt;&gt;&gt;&gt;(.*)$'
def _iindent3_repl(mastr):
    return ur'<div class="indent3">' + mastr + ur'</div>'

iindent3 = ReplacePattern(_iindent3_pattern, _iindent3_repl)

_iindent2_pattern = r'^&gt;&gt;&gt;&gt;([\s\S]+)$'
def _iindent2_repl(mastr):
    return ur'<div class="indent2">' + mastr + ur'</div>'

iindent2 = ReplacePattern(_iindent2_pattern, _iindent2_repl)

_iindent1_pattern = r'^&gt;&gt;([\s\S]+)$'
def _iindent1_repl(mastr):
    return ur'<div class="indent1">' + mastr + ur'</div>'

iindent1 = ReplacePattern(_iindent1_pattern, _iindent1_repl)
