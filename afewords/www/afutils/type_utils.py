#coding=utf-8

def type_trans(src):
    '''for frontend and backend type translations'''
    from article.blog import Blog
    from article.comment import Comment
    from article.equation import Equation
    from article.langcode import Langcode
    from article.reference import Reference
    from article.picture import Picture
    from article.tableform import Tableform
    from user import User
    trans_doc = {
        'blog' : Blog.__name__,
        'user' : User.__name__,
        'comment' : Comment.__name__,
        'math' : Equation.__name__,
        'code' : Langcode.__name__,
        'ref' : Reference.__name__,
        'img' : Picture.__name__,
        'table' : Tableform.__name__,
    }
    try:
        return trans_doc[src]
    except KeyError:
        return None
