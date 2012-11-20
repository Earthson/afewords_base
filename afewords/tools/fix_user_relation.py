#!/usr/bin/env python
from user import User
from article.blog import Blog
from datetime import datetime

usrs = [User(data=each) for each in User.datatype.find()]
for each in usrs:
    each.lib.follow_user_lib.clear()
    each.lib.follower_user_lib.clear()
    each.lib.follow_group_lib.clear()
    catalog_lib = each.lib.managed_catalog_lib
    tmp = catalog_lib.load_all()
    if tmp is None:
        tmp = dict()
    for ek, ev, in tmp.items():
        tmp[ek] = [ev, datetime.now()]
    catalog_lib.set_all(tmp)
