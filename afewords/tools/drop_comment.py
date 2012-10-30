#!/usr/bin/env python
from article.comment import Comment

com_all = [Comment(each) for each in Comment.datatype.find()]
for each in com_all:
    each.remove()
