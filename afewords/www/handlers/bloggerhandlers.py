#coding=utf-8

from basehandler import *
from pages.bloggerpage import BloggerBlogPage
from afutils.page_utils import page_split


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
        page['tag_list'] = author.lib.tag_lib['alltags']
        page['current_tag'] = paras['tag']
        blogs_info = author.blogs_info_view_by(usr, page['current_tag'])
        page['blog_list'], page['page_list'] = page_split(blogs_info,
                        page['current_page'], 10)
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

class BloggerBookHandler(BaseHandler):
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
