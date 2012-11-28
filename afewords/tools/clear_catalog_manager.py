#!/usr/bin/env python

from article.catalog import Catalog

catalogall = [Catalog(data=each) for each in Catalog.datatype.find()]

for each in catalogall:
    each.managers = list()
