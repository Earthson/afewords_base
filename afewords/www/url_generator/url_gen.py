from gen_utils import *

gen_list = [blog_gen(), user_gen()]


def url_gen(obj):
    mapper = dict(gen_list)
    if obj.__class__.__name__ not in mapper:
        return ''
    return mapper[obj.__class__.__name__](obj)
