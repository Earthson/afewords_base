#!/usr/bin/env python
from user import User

usrs = [User(data=each) for each in User.datatype.find()]
for each in usrs:
    if 'account_status' not in each.data:
        each.account_status = 'normal'
