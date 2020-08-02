import requests
import a_a_parameters_connection as pc
import c_a_parameters_bible as pb
import json
import os
from tinydb import TinyDB, Query

url = pc.BASE_API_URL + '/v1/bibles/' + pb.BIBLE_ID + '/books'

headers = {'api-key': pc.API_KEY}
r = requests.get(url, headers=headers)

#creating bible folder
if not os.path.exists(pb.BIBLE_ID):
    os.mkdir(pb.BIBLE_ID)


books_dict = json.loads(r.text)

db = TinyDB(pb.BIBLE_ID + '/c_c_db_'+pb.BIBLE_ID+'_books.json')
db.truncate()

for book in books_dict['data']:
    db.insert(book)

print(len(db))


