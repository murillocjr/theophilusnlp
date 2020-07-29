from tinydb import TinyDB, Query

db = TinyDB('db_bibles.json')

#Bible = Query()
#cc = db.count(Bible.name == 'Geneva Bible')
#print(cc)

for item in db:
    print(item['id'] + '|' + item['name'])


