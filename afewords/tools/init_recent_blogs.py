#!/usr/bin/env python

from global_info import recent_blogs
from article.blog import Blog

blog_all = [Blog(each) for each in Blog.datatype.find()]
blog_all = sorted(blog_all, reverse=True)
for each in blog_all:
    recent_blogs.push(each._id)
    recent_blogs.pop_head()
