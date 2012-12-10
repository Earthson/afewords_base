#!/usr/bin/env python
from article.blog import Blog
from user import User

bids = ['5020dbdb37251703ac000005', '502266ba3725170e83000002', '502267a83725170e82000002', '502267a83725170e85000002', '50226ddd3725170ef3000003', '50227fef3725170f90000008']

blogobjs = Blog.by_ids(bids)
user_af = User.find_one({'email':'afewords@afewords.com'})
for each in blogobjs:
    each.set_propertys(env=user_af, author=user_af)
    user_af.add_tags(each.tag)
    user_af.post_blog(each)
