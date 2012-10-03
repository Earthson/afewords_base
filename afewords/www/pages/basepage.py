def with_attr(cls):
    try:
        doc = super(cls, cls).doc
        doc.update(cls.doc)
        cls.doc = doc
        return cls
    except AttributeError:
        return cls

@with_attr
class BasePage(object):
    __template__ = ''
    doc = {}

    def __init__(self, handler, doc=None):
        self.handler = handler
        self.doc = dict(self.doc)
        if doc:
            self.doc.update(doc)

    def render(self):
        return self.handler.render(self.__template__, doc=self.doc)

    show = render

    def render_string(self):
        return self.handler.render_string(self.__template__, doc=self.doc)

    __unicode__ = render_string
    __str__ = render_string
