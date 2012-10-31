#!/usr/bin/env python

from article.catalog import Catalog

all_catalogs = [Catalog(each) for each in Catalog.datatype.find()]
for each in all_catalogs:
    each.about.env = each
