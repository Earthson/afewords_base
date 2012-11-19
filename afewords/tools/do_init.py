#!/usr/bin/env python

import os
for each in os.popen('ls *.py'):
    if each == 'fix.py\n' or each == 'do_init.py\n':
        continue
    print('running...: %s' % each[:-1])
    info = os.popen('python2 ' + each[:-1])
    print('end: %s' % each[:-1])
