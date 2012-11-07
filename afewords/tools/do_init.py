#!/usr/bin/env python

import os
for each in os.popen('ls *.py'):
    if each == 'fix.py\n' or each == 'do_init.py\n':
        continue
    info = os.popen('python2 ' + each)
    print(''.join(e for e in info))
