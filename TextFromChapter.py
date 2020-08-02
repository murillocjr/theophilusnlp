import json
import c_a_parameters_bible as pb
from tinydb import TinyDB, Query

def wholeChapter(chapter_id):
    db_chapter = TinyDB(pb.BIBLE_ID + '/e_c_db_'+pb.BIBLE_ID+'_'+ chapter_id +'.json')

    verses_text = [] 

    for record in db_chapter:
        for content in record['content']:
            for item in content['items']:
                verses_text.append(item['text'])

    return ''.join(verses_text)

