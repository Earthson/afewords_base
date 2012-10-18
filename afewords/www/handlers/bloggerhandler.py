#coding=utf-8

from basehandler import *
from pages.bloggerpage import BloggerPage


class BloggerHandlerPara(BaseHandlerPara):
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

class BloggerHandler(BaseHandler):

    def get(self, uid):
        pass
