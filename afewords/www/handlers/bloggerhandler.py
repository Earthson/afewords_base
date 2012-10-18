#coding=utf-8

from basehandler import *
from pages.bloggerpage import BloggerBlogPage


class BloggerBlogPara(BaseHandlerPara):
    paradoc = {
        'page' : 1,
        'tag' : 'default',
    }
    
    def read(self):
        try:
            self['page'] = int(self.handler.get_esc_arg('page', self['page']))
        except:
            self['page'] = 1
        self.['tag'] = self.handler.get_esc_arg('tag', self['tag'])

    def verify(self):
        return 0

class BloggerBlogHandler(BaseHandler):

    def get(self, uid):
        from user import User
        usr = self.current_user
        if uid is None:
            if usr is None:
                self.redirect('/')    
                return
            author = usr
        else:
            author = User.by_id(uid)
            if author is None:
                self.send_error(404)
                return
        paras = BloggerBlogPara(self)
        page = BloggerBlogPage(self)
        page['current_page'] = paras['page']
        if usr:
            page['author'] = usr.as_viewer(author)
        else:
            page['author'] = author.basic_info
        page['tag_list'] = author.lib.tag_lib.keys()
        page['current_tag'] = paras['tag']
        paradoc = dict()
        if para['tag'] != 'default':
            paradoc['tag'] = para['tag']
