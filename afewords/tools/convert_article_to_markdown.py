#!/usr/bin/env python

from article.translator.trans import normal_translator
from article.blog import Blog
from article.about import About
from article.comment import Comment
from article.reference import Reference
from article.tableform import Tableform

translate = normal_translator.translate

blogs_all = [Blog(each) for each in Blog.datatype.find()]
comments_all = [Comment(each) for each in Comment.datatype.find()]
about_all = About.find()
ref_all = Reference.find()
table_all = Tableform.find()


for each in blogs_all + comments_all + about_all:
    each.abstract = translate(each.abstract)
    each.body = translate(each.body)

for each in ref_all:
    each.body = translate(each.body)

for each in table_all:
    each.tableform = translate(each.tableform)
