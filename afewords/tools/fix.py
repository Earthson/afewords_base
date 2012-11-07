#!/usr/bin/env python

import os
for each in os.popen('ls fix_*.py'):
    info = os.popen('python2 ' + each) 
    print(''.join(e for e in info))
