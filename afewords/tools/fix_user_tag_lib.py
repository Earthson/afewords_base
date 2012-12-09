#!/usr/bin/env python

from user import User
from article.blog import Blog

user_all = [User(each) for each in User.datatype.find()]

for each in user_all:
    tag_lib = each.lib.tag_lib
    tmp = tag_lib.load_all()
    for tag in tmp.keys():
        if tag == u'alltags':
            continue
        if not tmp[tag]:
            continue
        tmp[tag] = [[e._id, e.release_time]
                for e in Blog.by_ids(
                    [each[0] if isinstance(each, list) else each 
                    for each in tmp[tag]])]
    tag_lib.set_all(tmp)
