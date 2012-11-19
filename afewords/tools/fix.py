#!/usr/bin/env python

import os
for each in os.popen('ls fix_*.py'):
    print('running...: %s' % each[:-1])
    info = os.popen('python2 ' + each[:-1]) 
    print('end: %s' % each[:-1])
    #print(''.join(e for e in info))
