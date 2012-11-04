#!/usr/bin/env python

from article.blog import Blog
from article.comment import Comment

blogs_all = [Blog(each) for each in Blog.datatype.find()]
comments_all = [Comment(each) for each in Comment.datatype.find()]

for each in blogs_all+comments_all:
    each.body_version += 1
