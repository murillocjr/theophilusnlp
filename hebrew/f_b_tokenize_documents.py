import pymongo
from bson.objectid import ObjectId

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import sqlite3

#### target database
conn = sqlite3.connect('f_c_db_tanach.sqlite')
cur = conn.cursor()
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='wordtokens' ''')
if cur.fetchone()[0]==1 : {
	cur.execute('DROP TABLE wordtokens;')
}
cur.execute('CREATE TABLE IF NOT EXISTS wordtokens (id integer PRIMARY KEY, token text NOT NULL, book text NOT NULL, chapter text NOT NULL);')
####

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sefaria"]
mycol = mydb["texts"]

# Books
books_query = {"language": "he", "versionTitle": "Tanach with Text Only"}
books = mycol.find(books_query)

for book in books:
    book_name = book['title']
    chapters = book['chapter']

    fragments = []
    chapter_number = 1

    for chapter in chapters:
        for verse in chapter:
            fragments.append(verse)

        chapter_text = ''.join(fragments)
        tokens = word_tokenize(chapter_text)

        for token in tokens:
            cur.execute('INSERT INTO wordtokens (token, book, chapter) values(\'' + token + '\',\''+ book_name + '\',\'' + str(chapter_number) +'\');')
                    
        chapter_number += 1

    print(book_name + ' ' + str(chapter_number))

conn.commit()
conn.close()
