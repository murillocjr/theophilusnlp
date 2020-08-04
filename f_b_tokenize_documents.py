from tinydb import TinyDB, Query
import c_a_parameters_bible as pb
from TextFromChapter import wholeChapter
from nltk.tokenize import word_tokenize
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect(pb.BIBLE_ID + '/f_c_db_'+pb.BIBLE_ID+'.sqlite')
cur = conn.cursor()
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='wordtokens' ''')
if cur.fetchone()[0]==1 : {
	cur.execute('DROP TABLE wordtokens;')
}
cur.execute('CREATE TABLE IF NOT EXISTS wordtokens (id integer PRIMARY KEY, token text NOT NULL);')


db_chapters = TinyDB(pb.BIBLE_ID + '/d_c_db_'+pb.BIBLE_ID+'_chapters.json')

for chapter in db_chapters:
    chapter_text = wholeChapter(chapter['id'])
    tokens = word_tokenize(chapter_text)
    print(chapter['bookId']+': '+str(len(tokens)))
    for token in tokens:
        cur.execute('INSERT INTO wordtokens (token) values(\'' + token + '\');')

    if chapter['bookId'] != 'GEN': break

conn.commit()
conn.close()
