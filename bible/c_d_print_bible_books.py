from tinydb import TinyDB, Query
import c_a_parameters_bible as pb

db = TinyDB(pb.BIBLE_ID + '/c_c_db_'+pb.BIBLE_ID+'_books.json')

for book in db:
    print(book['id'] + '|' + book['name'])


