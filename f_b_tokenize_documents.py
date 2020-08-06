from tinydb import TinyDB, Query
import c_a_parameters_bible as pb
from TextFromChapter import wholeChapter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect(pb.BIBLE_ID + '/f_c_db_'+pb.BIBLE_ID+'.sqlite')
cur = conn.cursor()
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='wordtokens' ''')
if cur.fetchone()[0]==1 : {
	cur.execute('DROP TABLE wordtokens;')
}
cur.execute('CREATE TABLE IF NOT EXISTS wordtokens (id integer PRIMARY KEY, token text NOT NULL, book text NOT NULL, chapter text NOT NULL);')

stop_words = set(stopwords.words('english'))
db_chapters = TinyDB(pb.BIBLE_ID + '/d_c_db_'+pb.BIBLE_ID+'_chapters.json')

for chapter in db_chapters:
#    if chapter['id'] != 'NUM.21':
#        continue

    chapter_text = wholeChapter(chapter['id'])

    tokens = word_tokenize(chapter_text)
    non_punctuation_tokens = [token for token in tokens if token.isalnum()]
    removed_stop_words = [w for w in non_punctuation_tokens if not w.lower() in stop_words] 

    print(chapter['id']+': '+str(len(removed_stop_words)))
    for token in removed_stop_words:
        cur.execute('INSERT INTO wordtokens (token, book, chapter) values(\'' + token + '\',\''+ chapter['bookId'] + '\',\'' + chapter['id'] +'\');')

#    if chapter['bookId'] != 'GEN': break

conn.commit()
conn.close()
