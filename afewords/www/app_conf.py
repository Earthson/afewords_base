#coding=utf-8
import os
from handlers.indexhandler import IndexHandler
from handlers.logcontrolhandlers import LoginHandler
from handlers.logcontrolhandlers import LogoutHandler
from handlers.securityhandlers import VertifyCodeHandler
from handlers.securityhandlers import RegisterHandler
from handlers.testhandler import TestHandler
from handlers.securityhandlers import CheckHandler
from handlers.securityhandlers import ResetHandler, RepeatResetMailHandler
from handlers.bloghandler import BlogHandler
from handlers.bloggerhandlers import BloggerBlogHandler
from handlers.bloggerhandlers import BloggerBookHandler
from handlers.bloggerhandlers import BloggerAboutHandler
from handlers.articlewritehandlers import ArticleWriteHandler
from handlers.articlewritehandlers import ArticleUpdateHandler
from handlers.articlewritehandlers import ArticleSrcHandler
from handlers.articleremovehandlers import ArticleRemoveHandler
from handlers.commenthandlers import CommentGetHandler


from handlers.settingspagehandlers import UserSettingInviteHandler
from handlers.settingspagehandlers import UserSettingPasswordHandler
from handlers.settingspagehandlers import UserSettingDomainHandler
from handlers.settingspagehandlers import UserSettingAvatarHandler
from handlers.settingspagehandlers import UserSettingTagHandler
from handlers.settingspagehandlers import UserSettingNoticeHandler
from handlers.settingspagehandlers import UserSettingDraftHandler
from handlers.settingspagehandlers import UserSettingFollowHandler
from handlers.settingspagehandlers import UserSettingFollowerHandler

from handlers.settinguserhandlers import UserInviteHandler
from handlers.settinguserhandlers import UserDomainSettingHandler
from handlers.settinguserhandlers import UserPasswordSettingHandler
from handlers.settinguserhandlers import UserTagAddHandler
from handlers.settinguserhandlers import UserTagRemoveHandler
from handlers.settinguserhandlers import UserNotiReadAllHandler
from handlers.settinguserhandlers import UserNotiEmptyHandler
from handlers.settinguserhandlers import UserNotiReadHandler
from handlers.settinguserhandlers import UserNotiRemoveHandler
from handlers.settinguserhandlers import UserAvatarUploadHandler
from handlers.settinguserhandlers import UserAvatarCropHandler

from handlers.bookhandlers import BookHandler
from handlers.bookhandlers import BookChapterHandler

from handlers.afbookhandlers import AFBookHandler
from handlers.afbookhandlers import AFUserBookHandler
from handlers.afbookhandlers import AFBookCreateHandler

app_handlers = {
    (r'/', IndexHandler), #MainHandler),
    (r'/test', TestHandler),
    #(r'/home', HomeHandler),
    (r'/home', BloggerBlogHandler),
    (r'/login', LoginHandler),
    (r'/quit', LogoutHandler),
    (r'/code', VertifyCodeHandler),
    (r'/reg', RegisterHandler),
    (r'/check', CheckHandler),
    (r'/reset', ResetHandler),
    (r'/repeat-mail', RepeatResetMailHandler),
    (r'/blog/(.+)', BlogHandler),
    (r'/blogger/([0-9a-zA-Z]+)/about', BloggerAboutHandler),
    (r'/blogger/([0-9a-zA-Z]+)/book', BloggerBookHandler),
    (r'/blogger/([0-9a-zA-Z]+)/blog', BloggerBlogHandler),
    (r'/blogger/([0-9a-zA-Z]+)', BloggerBlogHandler),
    (r'/blogger', BloggerBlogHandler),
    (r'/user/([_0-9a-zA-Z]+)', BloggerBlogHandler),
    (r'/write', ArticleWriteHandler),
    (r'/update-article', ArticleUpdateHandler),
    (r'/article-src-control', ArticleSrcHandler),
    (r'/getcomment', CommentGetHandler),
    #(r'/home(.*)', UserBlogLibHandler),
    (r'/settings-invite', UserSettingInviteHandler),
    (r'/settings-password', UserSettingPasswordHandler),
    (r'/settings-domain', UserSettingDomainHandler),
    (r'/settings-avatar', UserSettingAvatarHandler),
    (r'/settings-tag', UserSettingTagHandler),
    (r'/notice', UserSettingNoticeHandler),
    (r'/draft', UserSettingDraftHandler),
    (r'/settings-follow', UserSettingFollowHandler),
    (r'/settings-follower', UserSettingFollowerHandler),
    (r'/book/([0-9a-zA-Z]+)', BookHandler),
    (r'/book/([0-9a-zA-Z]+)/catalog/([0-9]+)', BookChapterHandler),

    (r'/afewords-book', AFBookHandler),
    (r'/user-book', AFUserBookHandler),
    (r'/book-create', AFBookCreateHandler),

    (r'/settingpost-article_remove', ArticleRemoveHandler),

    (r'/settingpost-invite', UserInviteHandler),
    (r'/settingpost-user_domain', UserDomainSettingHandler),
    (r'/settingpost-user_passwd', UserPasswordSettingHandler),
    (r'/settingpost-user_addtag', UserTagAddHandler),
    (r'/settingpost-user_removetag', UserTagRemoveHandler),
    (r'/settingpost-user_noti_markall', UserNotiReadAllHandler),
    (r'/settingpost-user_noti_empty', UserNotiEmptyHandler),
    (r'/settingpost-user_noti_read', UserNotiReadHandler),
    (r'/settingpost-user_noti_remove', UserNotiRemoveHandler),
    (r'/settingpost-user_avatar_upload', UserAvatarUploadHandler),
    (r'/settingpost-user_avatar_crop', UserAvatarCropHandler),
}

app_settings = {
    'static_path' : os.path.join(os.path.dirname(__file__), "static"),
    'template_path' : os.path.join(os.path.dirname(__file__), "templates"),
    #'debug' : True,
    'cookie_secret' : '11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=',
    'login_url' : '/login',
    'autoescape' : None,
    'xsrf_cookies' : True,
    'picture_domain' : 'picture1',
    #'localhost' : True,
}

