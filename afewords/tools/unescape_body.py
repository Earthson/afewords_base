#!/usr/bin/env python

from article.blog import Blog
from article.about import About
from article.comment import Comment
from article.reference import Reference
from article.tableform import Tableform
from article.langcode import Langcode

from tornado.escape import xhtml_unescape

blogs_all = [Blog(each) for each in Blog.datatype.find()]
comments_all = [Comment(each) for each in Comment.datatype.find()]
about_all = About.find()
ref_all = Reference.find()
table_all = Tableform.find()
code_all = Langcode.find()


for each in blogs_all + comments_all + about_all:
    each.abstract = xhtml_unescape(each.abstract)
    each.body = xhtml_unescape(each.body)

for each in ref_all:
    each.body = xhtml_unescape(each.body)

for each in code_all:
    each.code = xhtml_unescape(each.code)

for each in table_all:
    each.tableform = xhtml_unescape(each.tableform)
