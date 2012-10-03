from basepage import BasePage, with_attr

@with_attr
class LoginPage(BasePage):
    '''
    title: what is title?
    blog_list: what is blog_list?
    ...
    '''
    __template_file__ = 'afewords.html'

    doc = {
        'title' : '子曰 - 执笔写下收获',
        #what is title? doc
        'blog_list' : None,
    }
