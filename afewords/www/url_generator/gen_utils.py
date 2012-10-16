

def blog_gen():
    from article.blog import Blog
    def gen(obj):
        return '/blog/' + obj.uid
    return Blog.__name__, gen

def user_gen():
    from user import User
    def gen(obj):
        return '/home/' + obj.uid
    return User.__name__, gen
