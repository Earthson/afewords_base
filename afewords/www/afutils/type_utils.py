#coding=utf-8

def type_trans(src):
    '''for frontend and backend type translations'''
    from article.blog import Blog
    from article.comment import Comment
    from user import User
    trans_doc = {
        'blog' : Blog.__name__,
        'user' : User.__name__,
        'comment' : Comment.__name__,
    }
    try:
        return trans_doc[src]
    except KeyError:
        return None
