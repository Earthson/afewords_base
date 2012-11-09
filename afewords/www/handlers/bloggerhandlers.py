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


class BaseBloggerHandler(BaseHandler):
    def get_init(self, uid=None):
        from user import User
        usr = self.current_user
        self.usr= usr
        if uid is None:
            if usr is None:
                self.redirect('/login')
                return
            self.author = usr
        else:
            self.author = User.by_id(uid)
            if self.author is None:
                self.author = User.find_one({'domain':uid})
            if self.author is None:
                self.send_error(404)
                return


class BloggerBlogHandler(BaseBloggerHandler):

    def get(self, uid=None):
        self.get_init(uid)
        usr = self.current_user
        author = self.author
        paras = BloggerBlogPara(self)
        page = BloggerBlogPage(self)
        page['current_page'] = paras['page']
        if usr:
            page['author'] = usr.as_viewer(author)
        else:
            page['author'] = author.basic_info
        page['tag_list'] = author.alltags
        page['current_tag'] = paras['tag']
        enum = 7
        page['blog_list'], blog_cnt = author.blogs_info_view_by(usr, 
                page['current_tag'], vfrom=enum*(page['current_page']-1), 
                vlim=enum)
        page['page_list'] = [i/enum + 1 for i in range(0, blog_cnt, enum)]
        #for paging support 
        paradoc = dict()
        if paras['tag'] != 'default':
            paradoc['tag'] = paras['tag']
        page['urlparas'] = paradoc
        page['baseurl'] = self.request_url
        page.page_init()
        page.render()
        return


from pages.bloggerpage import BloggerBookPage

class BloggerBookHandler(BaseBloggerHandler):
    def get(self, uid=None):   
        self.get_init(uid)
        usr = self.usr
        author = self.author
        handler_page = BloggerBookPage(self)
        if usr:
            handler_page['author'] = usr.as_viewer(author)
        else:
            handler_page['author'] = author.basic_info
        handler_page['book_list'] = [each.basic_info 
                for each in author.managed_catalogs]
        handler_page.page_init()
        handler_page.render()
        return

from pages.bloggerpage import BloggerAboutPage

class BloggerAboutHandler(BaseBloggerHandler):
    def get(self, uid=None):
        self.get_init(uid)
        usr = self.usr
        author = self.author
        handler_page = BloggerAboutPage(self)
        handler_page['author'] = usr.as_viewer(author) \
                    if usr else author.basic_info
        handler_page['about'] = author.about.basic_info
        handler_page.page_init()
        handler_page.render()
        return
