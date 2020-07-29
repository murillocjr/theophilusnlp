from tinydb import TinyDB, Query
import parameters

db = TinyDB('db_'+parameters.BIBLE_ID+'.json')

for item in db:
    print(item)


