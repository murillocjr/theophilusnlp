
from tinydb import TinyDB, Query
import json

db = TinyDB('db_bibles.json')
db.truncate()

with open('available-bibles.json', 'r') as f:
    bibles_dict = json.load(f)

for bible in bibles_dict['data']:
    db.insert(bible)

print(len(db))

