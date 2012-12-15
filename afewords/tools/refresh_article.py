#!/usr/bin/env python

from article.blog import Blog
from article.comment import Comment
from article.reference import Reference
from article.about import About

blogs_all = [Blog(each) for each in Blog.datatype.find()]
comments_all = [Comment(each) for each in Comment.datatype.find()]
about_all = About.find()
ref_all = Reference.find()

for each in blogs_all+comments_all+about_all+ref_all:
    try:
        if isinstance(each.author_id, basestring):
            each.remove()
            continue
    except:
        pass
    finally:
        each.body_version += 1
