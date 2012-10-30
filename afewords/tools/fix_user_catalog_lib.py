#!/usr/bin/env python
from user import User

usrs = [User(data=each) for each in User.datatype.find()]
for each in usrs:
    tmp = each.lib.managed_catalog_lib.load_all()
    if tmp:
        for ek in tmp.keys():
            tmp[ek] = 'owner'
        each.lib.managed_catalog_lib.set_all(tmp)
        print tmp
