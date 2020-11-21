import sys
sys.path.append('../commons/')
from get_lemma import getLemma
from stop_words import getStopWords

import pymongo
import a_parameters as pr
from bson.objectid import ObjectId
from nltk.tokenize import word_tokenize
from collections.abc import Mapping
from nltk.corpus import wordnet as wn
import gensim
from gensim import corpora
import pickle
import os
import json

def searchText(obj):
    if (type(obj) is str):
        processText(obj)
    elif (type(obj) is list):
        for item in obj:
            searchText(item)
    elif (type(obj) is dict):
        for key_k in obj.keys():
            searchText(obj[key_k])
    else:        
        print(type(obj))

def processText(text):
    tokens = word_tokenize(text)
    
    non_punctuation_tokens = [token for token in tokens if token.isalnum()]
    removed_stop_words = [w for w in non_punctuation_tokens if not w.lower() in stop_words] 

    ch_tokens = []
    for word in removed_stop_words:
        ch_tokens.append(getLemma(word))

    text_data.append(ch_tokens)


text_data = []
stop_words = getStopWords('../commons/stop_words')


try:
    client = pymongo.MongoClient(pr.CON_STRING)
    client.server_info()  
except pymongo.errors.ServerSelectionTimeoutError as err:
    print(err)
    quit()

mydb = client.sefaria
mycol = mydb.texts
 
for doc_id in pr.DOC_IDS:
    metadataPath = '../models/'+doc_id+'.metadata'
    if os.path.exists(metadataPath):
        print('Already Processed: '+doc_id)
        continue
    print('Start processing: '+doc_id)

    document = mycol.find_one({'_id': ObjectId(doc_id)})
    searchText(document)

    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    pickle.dump(corpus, open('../models/'+doc_id+'_corpus.pkl', 'wb'))
    dictionary.save('../models/'+doc_id+'_dict.gensim')

    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = pr.TOPICS_NUMBER, id2word=dictionary, passes=pr.PASSES_COUNT)
    ldamodel.save('../models/'+doc_id+'_model5.gensim')
    topics = ldamodel.print_topics(num_words=pr.WORDS_NUMBER)
    # for topic in topics:
    #     print(topic)
    metadata = {}
    metadata['title'] = document['title']
    metadata['isScanned'] = False
    metadata['pagesCount'] = 0
    metadata['md5'] = doc_id
    metaFile = open('../models/'+doc_id+'.metadata', "w")
    metaFile.write(json.dumps(metadata))
    metaFile.close()
