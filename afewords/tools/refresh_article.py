#!/usr/bin/env python

from article.blog import Blog
from article.comment import Comment
from article.reference import Reference

blogs_all = [Blog(each) for each in Blog.datatype.find()]
comments_all = [Comment(each) for each in Comment.datatype.find()]
ref_all = Reference.find()

for each in blogs_all+comments_all+ref_all:
    each.body_version += 1
