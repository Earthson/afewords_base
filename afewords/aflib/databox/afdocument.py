from mongokit import Document

class AFDocument(Document):
    use_schemaless = True
    structure = {
        'data_status' : basestring,
    }
    default_values = {
        'data_status' : 'normal',
    }

    def __getitem__(self, key):
        try:
            return Document.__getitem__(self, key)
        except KeyError:
            self[key] = self.default_values[key]
            return self.default_values[key]

    def remove(self):
        #self['data_status'] = 'removed'
        #self.save()
        self.delete()
