from emmongodict import EmMongoDict
foo = EmMongoDict()
foo['one'] = 'Sample'
foo['bar'] = [1, 2, 3]
foo['em'] = {'x':1, 'y':2}
foo['one']
foo['bar']
foo['em']
from emmongolist import EmMongoList
samplelist = foo.sublist('bar')
samplelist.load_list()
samplelist[0] = 100
print samplelist.load_list()
print samplelist[0]
samplelist[2] += 200
samplelist.load_list()
samplelist.push(10000)
samplelist.push(20000, 30000, 40000)
print samplelist.load_list()
print samplelist.pop()
print samplelist.load_list()
print samplelist.pop_head()
print samplelist.load_list()
samplelist.pull(203)
del samplelist[3]
print samplelist.load_list()
samplelist.add_to_set(20000, 20001)
print samplelist.load_list()
emdict = foo.subdict('em')
emdict.load_doc()
emdict['x'] += 100
emdict['y'] += 100
emdict['z'] = 200
print emdict['m']
emdict['m'] = 2000
emdict.load_doc()
del emdict['m']
emdict.load_doc()
print emdict.pop('z')


class StudentDoc(EmMongoDict):
    db_info = {
        'db':'School',
        'collection':'StudentDocCCC',
    }
    indexes = {
        'email':{'unique':True, 'sparse':True},
    }

StudentDoc.init_collection()
StudentDoc.ensure_index()

s0 = StudentDoc(doc={'email':'a@a.com'})
print s0.spec
s1 = StudentDoc(doc={'email':'b@b.com'})
tmp = StudentDoc(spec={'email':'a@a.com'})
tmp['_id']
tmp['email']
tmp['test'] = 'hahaha'

print tmp.load_doc()
print s0.load_doc()
print s1.load_doc()

    
