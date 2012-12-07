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
        print(tmp[tag])
        if not tmp[tag]:
            continue
        if not isinstance(tmp[tag][0], list):
            tmp[tag] = [(e._id, e.release_time) for e in Blog.by_ids(tmp[tag])]
    tag_lib.set_all(tmp)
