#coding=utf-8

from basepage import BasePage, with_attr

@with_attr
class UserSettingsPage(BasePage):
    __template_file__ = 'settings/setting-base.html'
    doc = {
        'page_type': 'settings',
        'settings_type' : '',
        'current_page' : 1, # int , current page
        'paging_html' : '', # unicode , for paging 
        'title': '个人资料 - 子曰',
    }


@with_attr
class UserSettingInvitePage(UserSettingsPage):
    __template_file__ = 'afewords-user/user-invite.html'
    doc = {
        'settings_type' : 'invite',
        'page_type': 'user',
        'subpage_type': 'invite',
        'invite_count' : 0,
        'title': '邀请 - 子曰',
    }
    

@with_attr
class UserSettingPasswordPage(UserSettingsPage):
    __template_file__ = 'settings/setting-password.html'
    doc = {
        'settings_type' : 'password',
        'subpage_type': 'password',
        'title': '密码 - 子曰',
    }


@with_attr
class UserSettingDomainPage(UserSettingsPage):
    __template_file__ = 'settings/setting-domain.html'
    doc = {
        'settings_type' : 'domain',
        'subpage_type': 'domain',
        'domain' : '',
        'title': '个人链接 - 子曰',
    }


@with_attr
class UserSettingAvatarPage(UserSettingsPage):
    __template_file__ = 'settings/setting-avatar.html'
    doc = {
        'settings_type' : 'avatar',
        'subpage_type': 'avatar',
        'avatar_path' : '',
        'title': '头像 - 子曰'
    }


@with_attr
class UserSettingFollowPage(UserSettingsPage):
    __template_file__ = 'afewords-user/user-follow.html'
    doc = {
        'settings_type' : 'follow',
        'subpage_type': 'follow',
        'follow_list' : [], # see [[ follow_list ]] in data_format
        'title': '我关注 - 子曰'
    }


@with_attr
class UserSettingTagPage(UserSettingsPage):
    __template_file__ = 'settings/setting-tag.html'
    doc = {
        'settings_type' : 'tag',
        'subpage_type': 'tag',
        'tag_list' : [],   # see [[ tag_list ]] in data_format
        'title': '执笔分类 - 子曰',
    }


@with_attr
class UserSettingFollowerPage(UserSettingsPage):
    __template_file__ = 'afewords-user/user-follower.html'
    doc = {
        'settings_type' : 'follower',
        'subpage_type': 'follower',
        'follower_list' : [],   # see [[ follower_list ]] in data_format
        'title': '关注我 - 子曰',
    }


@with_attr
class UserSettingNoticePage(UserSettingsPage):
    __template_file__ = 'settings/setting-notice.html'
    doc = {
        'settings_type' : 'notice',
        'subpage_type': 'notice',
        'notice_list' : [], # see [[ notice_list ]] in data_format
        'title': '消息 - 子曰',
    }


@with_attr
class UserSettingDraftPage(UserSettingsPage):
    __template_file__ = 'settings/setting-draft.html'
    doc = {
        'settings_type' : 'draft',
        'subpage_type': 'draft',
        'draft_list' : [],  # see [[ draft_list ]] in data_format
        'title': '草稿 - 子曰',
    }
