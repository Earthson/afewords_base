#!/usr/bin/env python
from user import User
from article.blog import Blog

usrs = [User(data=each) for each in User.datatype.find()]
for each in usrs:
    blogs = Blog.by_ids(each.lib.blog_list.load_all())
    for eb in blogs:
        eb.env = each
        eb.author = eb.author
        each.reset_blog_tags(eb)
