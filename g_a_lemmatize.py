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

conn = sqlite3.connect(pb.BIBLE_ID + '/f_c_db_'+pb.BIBLE_ID+'.sqlite')
cur = conn.cursor()
cur.execute(''' SELECT token, count(*) as 'count' FROM wordtokens GROUP BY token ORDER by 2 desc limit 20; ''')

text_data = []

for row in cur:
	#print(row[0], get_lemma(row[0]))
	text_data.append(get_lemma(row[0]))

dictionary = corpora.Dictionary(text_data)corpus = [dictionary.doc2bow(text) for text in text_data]
pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')


conn.commit()
conn.close()
