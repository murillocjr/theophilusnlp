import requests
import a_a_parameters_connection as pc
import c_a_parameters_bible as pb
import json
import os
from tinydb import TinyDB, Query

db_chapters = TinyDB(pb.BIBLE_ID + '/d_c_db_'+pb.BIBLE_ID+'_chapters.json')
db_chapters.truncate()

db_books = TinyDB(pb.BIBLE_ID + '/c_c_db_'+pb.BIBLE_ID+'_books.json')
headers = {'api-key': pc.API_KEY}
for book in db_books:
    url = pc.BASE_API_URL + '/v1/bibles/' + pb.BIBLE_ID + '/books/' + book['id'] + '/chapters' 
    r = requests.get(url, headers=headers)
    chapters_dict = json.loads(r.text)
    for chapter in chapters_dict['data']:
        db_chapters.insert(chapter)
    print(book['id'] + ':' + str(len(chapters_dict['data'])))

print(len(db_chapters))


