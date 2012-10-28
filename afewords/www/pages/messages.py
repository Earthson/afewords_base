#coding=utf-8

from pages.basepage import BaseMSG, with_attr

@with_attr
class BeCommentedMSG(BaseMSG):
    doc = {
        'article_url': '',
        'article_title' : '',
        'comment_id' : '',
    }

    def comment_by(article_obj, comment_obj):
        self['article_url'] = article_obj.obj_url
        self['article_title'] = article_obj.name
        self['comment_id'] = comment_obj.uid
