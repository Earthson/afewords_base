import os


aflib_root = os.path.dirname(__file__)
if not aflib_root:
    aflib_root = '.'

pic_main_url = '/'
#pic_main_url = 'http://picture.afewords.com/'
main_url = '/'
#main_url = 'http://www.afewords.com'
supportedlangcode = dict()

def load_aflibconf(filename='aflib.conf'):
    try:
        ff = open(aflib_root+'/conf.d'+filename, 'r')
        exec(''.join(ff), globals())
    except IOError:
        print('file not found! aflib keeps original settings')
        

def load_supportedlangcode(filename='supportedlangcode.conf'):
    try:
        ff = open(aflib_root+'/conf.d/'+filename, 'r')
        supportedlangcode.update(eachline[:-1].split('=',1) for eachline in ff
                    if eachline[0] not in ['#', ' '])
    except IOError:
        print('file not found! supported langcode not load!')

load_supportedlangcode()
