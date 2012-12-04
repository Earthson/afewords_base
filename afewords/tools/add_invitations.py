#!/usr/bin/env python
'''
usage:
add_invitations count email
count is a number, email could be 'all'
'''

from user import User
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Invalid arguments: usage: command count email')
    count = int(sys.argv[1])
    email = sys.argv[2]
    if email == 'all':
        for each in User.find():
            each.invitations += count
    else:
        usr = User.find_one({'email':email})
        usr.invitations += count
