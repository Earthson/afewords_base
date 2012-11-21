#!/usr/bin/env python

from global_info import *
from article.blog import Blog
from article.catalog import Catalog
from user import User

recent_blogs.set_all([None for i in range(200)])
blog_all = sorted([Blog(each) 
                for each in Blog.datatype.find()], reverse=True)
for each in blog_all:
    recent_blogs.push(each._id)
    recent_blogs.pop_head()

recent_books.set_all([None for i in range(200)])
book_all = sorted([Catalog(each) 
                for each in Catalog.datatype.find()], reverse=True)
for each in book_all:
    recent_books.push(each._id)
    recent_books.pop_head()

recent_users.set_all([None for i in range(200)])
user_all = sorted([User(each) 
                for each in User.datatype.find()], reverse=True)
for each in user_all:
    recent_users.push(each._id)
    recent_users.pop_head()

unreg_users.set_all([None for i in range(5000)])
recent_feedbacks.set_all([None for i in range(200)])
