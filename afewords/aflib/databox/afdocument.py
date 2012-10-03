from mongokit import Document

class AFDocument(Document):
    use_schemaless = True
    structure = {
        'data_status' : basestring,
    }
    default_values = {
        'data_status' : 'normal',
    }

    def remove(self):
        #self['data_status'] = 'removed'
        #self.save()
        self.delete()
