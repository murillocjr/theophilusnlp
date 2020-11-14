from tinydb import TinyDB, Query
import c_a_parameters_bible as pb

db_chapters = TinyDB(pb.BIBLE_ID + '/d_c_db_'+pb.BIBLE_ID+'_chapters.json')

for chapter in db_chapters:
    print(chapter['id'] + '|' + chapter['reference'])


