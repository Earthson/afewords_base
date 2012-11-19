#!/usr/bin/env python

from article.catalog import Catalog

all_catalogs = [Catalog(each) for each in Catalog.datatype.find()]
for each in all_catalogs:
    each.about.set_propertys(env=each, author_id=each.owner_id)

from user import User
user_all = [User(each) for each in User.datatype.find()]
for each in user_all:
    each.about.set_propertys(env=each, author_id=each._id)
