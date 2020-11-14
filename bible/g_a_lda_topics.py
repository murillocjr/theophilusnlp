from tinydb import TinyDB, Query

import c_a_parameters_bible as pb
import sqlite3
from sqlite3 import Error

from nltk.corpus import wordnet as wn

from gensim import corpora
import pickle

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

db_chapters = TinyDB(pb.BIBLE_ID + '/d_c_db_'+pb.BIBLE_ID+'_chapters.json')

conn = sqlite3.connect(pb.BIBLE_ID + '/f_c_db_'+pb.BIBLE_ID+'.sqlite')
cur = conn.cursor()

text_data = []
for chapter in db_chapters:
    print(chapter['bookId'], chapter['id'])

    cur.execute('SELECT token FROM wordtokens WHERE book=\''+ chapter['bookId'] + '\' AND chapter=\'' + chapter['id'] + '\' ;')

    ch_tokens = []
    for row in cur:
        # print(row[0])
        ch_tokens.append(get_lemma(row[0]))

    text_data.append(ch_tokens)

    #break

dictionary = corpora.Dictionary(text_data)
corpus = [dictionary.doc2bow(text) for text in text_data]
pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')

import gensim
NUM_TOPICS = 10
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
ldamodel.save('model5.gensim')
topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)
