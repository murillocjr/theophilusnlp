import requests
import a_a_parameters_connection as pc
import c_a_parameters_bible as pb
import json
import os
from tinydb import TinyDB, Query

headers = {'api-key': pc.API_KEY}
db_chapters = TinyDB(pb.BIBLE_ID + '/d_c_db_'+pb.BIBLE_ID+'_chapters.json')
for chapter in db_chapters:
    db_chapter = TinyDB(pb.BIBLE_ID + '/e_c_db_'+pb.BIBLE_ID+'_'+ chapter['id'] +'.json')
    db_chapter.truncate()

    url = pc.BASE_API_URL + '/v1/bibles/' + pb.BIBLE_ID + '/chapters/' + chapter['id'] + '?content-type=json&include-notes=false&include-titles=false&include-chapter-numbers=false&include-verse-numbers=false&include-verse-spans=false' 
    r = requests.get(url, headers=headers)
    chapter_dict = json.loads(r.text)

    db_chapter.insert(chapter_dict['data'])
    print(chapter['id'])

print(len(db_chapters))


