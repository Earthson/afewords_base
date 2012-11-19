#!/usr/bin/env python

from article.catalog import Catalog

catalog_all = [Catalog(each) for each in Catalog.datatype.find()]

for each in catalog_all:
    each.remove_count = each.node_count - len(each.lib.node_lib)
    each.complete_count = 0
    for ek, ev in each.lib.node_info_lib.load_all().items():
        each.get_node_dict(ek)['article_count'] = len(ev['articles'])
        each.get_node_dict(ek)['subcatalog_count'] = len(ev['catalogs'])
        each.get_node_dict(ek)['spec_count'] = len(ev['main'])
        if len(ev['main']) != 0:
            each.complete_count += 1
