#!/usr/bin/env python
from user import User

usrs = [User(data=each) for each in User.datatype.find()]
for each in usrs:
    each.account_status = 'normal'
