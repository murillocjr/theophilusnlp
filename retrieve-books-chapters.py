import requests
import parameters
import json
from tinydb import TinyDB, Query

bible_id = parameters.BIBLE_ID
url = 'https://api.scripture.api.bible/v1/bibles/' + bible_id + '/books'

headers = {'api-key': parameters.API_KEY}
r = requests.get(url, headers=headers)

#print(r.text)
books_dict = json.loads(r.text)

db = TinyDB('db_'+parameters.BIBLE_ID+'.json')
db.truncate()

for book in books_dict['data']:
    db.insert(book)

print(len(db))


