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
        self['tag'] = self.handler.get_esc_arg('tag', self['tag'])

    def verify(self):
        return 0

class BloggerBlogHandler(BaseHandler):

    def get(self, uid=None):
        from user import User
        usr = self.current_user
        if uid is None:
            if usr is None:
                self.redirect('/login')    
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
        try:
            page['tag_list'].remove('default')
        except ValueError:
            print 'tag: default not exist'
            pass
        page['current_tag'] = paras['tag']
        paradoc = dict()
        if paras['tag'] != 'default':
            paradoc['tag'] = para['tag']
        page['urlparas'] = paradoc
        each_page = 10
        st = each_page*page['current_page']
        ed = st + each_page
        blogs_info = author.blogs_info
        if usr:
            blogs_info = [author.as_viewer_to_article_info(each)
                            for each in blogs_info]
        page['blog_list'] = blogs_info
        page['page_list'] = [i/each_page + 1 
                        for i in range(0, len(blogs_info), each_page)]
        page['baseurl'] = self.request_url
        page.page_init()
        page.render()
        return
