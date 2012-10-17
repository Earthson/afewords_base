#coding=utf-8

from basepage import BasePage, with_attr

@with_attr
class GroupBasePage(BasePage):
    __template_file__ = 'group/group-base.html'
    doc = {
        'group': {},    # dict, see [[ group ]] in data_format
        'group_page':'index', # unicode, index, feedback, topic, bulletin,..
    }

@with_attr
class GroupIndexPage(GroupBasePage):
    __template_file__ = 'group/group-index.html'
    doc = {
        'group_page': 'index', # unicode str
        'topic_list': [],   # list, see [[ topic_list ]] in data_format
        'bulletin_list': [],    # list, see [[ bulletin_list ]] in data_format
    }

@with_attr
class GroupListBasePage(GroupBasePage):
    doc = {
        'current_page': 1,  # int
        'paging_html': '',  # unicode
    }

@with_attr
class GroupAboutPage(GroupListBasePage):
    __template_file__ = 'group/group-about.html'
    doc = {
        'group_page': 'about',  # unicode
        'about': {},    # dict, see [[ article ]], equal [[group]]['about']
    }


@with_attr
class GroupListFeedBackPage(GroupListBasePage):
    __template_file__ = 'group/group-list-feedback.html'
    doc = {
        'group_page': 'feedback', # unicode
        'feedback_list': [],    # list, see [[ feedback_list ]] in data_format
    }

@with_attr
class GroupListDocPage(GroupBasePage):
    __template_file__ = 'group/group-list-doc.html'
    doc = {
        'group_page': 'doc', # unicode
        'doc_list': [], # list, see [[ doc_list ]] in data_format
    } 

@with_attr
class GroupListBulletinPage(GroupBasePage):
    __template_file__ = 'group/group-list-bulletin.html'
    doc = {
        'group_page': 'bulletin', # unicode
        'bulletin_list': [],    # list, see [[ bulletin_list ]] in data_format
    }

@with_attr
class GroupListMemberPage(GroupBasePage):
    __template_file__ = 'group/group-list-member.html'
    doc = {
        'group_page': 'member', # unicode
        'member_list': [],  # list, see [[ member_list ]] in data_format
    }

@with_attr
class GroupListTopicPage(GroupBasePage):
    __template_file__ = 'group/group-list-topic.html'
    doc = {
        'group_page': 'topic', # unicode
        'topic_list': [],   # list, see [[ topic_list ]] in data_format
    }


@with_attr
class GroupFeedbackPage(GroupBasePage):
    __template_file__ = 'group/group-one-feedback.html'
    doc = {
        'group_page': 'feedback',   # 
        'feedback': {}, # dict, see [[ article ]] in data_format
    }


@with_attr
class GroupDocPage(GroupBasePage):
    __template_file__ = 'group/group-one-doc.html'
    doc = {
        'group_page': 'doc',   # 
        'doc': {}, # dict, see [[ article ]] in data_format
    }


@with_attr
class GroupBulletinPage(GroupBasePage):
    __template_file__ = 'group/group-one-bulletin.html'
    doc = {
        'group_page': 'bulletin',   # 
        'bulletin': {}, # dict, see [[ article ]] in data_format
    }


@with_attr
class GroupTopicPage(GroupBasePage):
    __template_file__ = 'group/group-one-topic.html'
    doc = {
        'group_page': 'topic',   # 
        'topic': {}, # dict, see [[ article ]] in data_format
    }

