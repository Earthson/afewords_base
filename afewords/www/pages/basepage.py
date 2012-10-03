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
    __template_file__ = ''
    doc = {}

    def __init__(self, handler, doc=None):
        self.handler = handler
        self.doc = dict(self.doc)
        if doc:
            self.doc.update(doc)

    def render(self):
        return self.handler.render(self.__template_file__, doc=doc)
