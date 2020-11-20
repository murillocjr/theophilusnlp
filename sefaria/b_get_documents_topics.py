import pymongo
import a_parameters as pr
from bson.objectid import ObjectId
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections.abc import Mapping
from nltk.corpus import wordnet as wn
from a_stopwords import getStopWords
import gensim
from gensim import corpora
import pickle

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
        ch_tokens.append(get_lemma(word))

    text_data.append(ch_tokens)

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

text_data = []
stop_words = getStopWords()


try:
    client = pymongo.MongoClient(pr.CON_STRING)
    client.server_info()  
except pymongo.errors.ServerSelectionTimeoutError as err:
    print(err)
    quit()

mydb = client.sefaria
mycol = mydb.texts
 
for doc_id in pr.DOC_IDS:
    document = mycol.find_one({'_id': ObjectId(doc_id)})
    searchText(document)

    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    pickle.dump(corpus, open('models/'+doc_id+'_corpus.pkl', 'wb'))
    dictionary.save('models/'+doc_id+'_dict.gensim')

    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = pr.NUM_TOPICS, id2word=dictionary, passes=30)
    ldamodel.save('models/'+doc_id+'_model5.gensim')
    topics = ldamodel.print_topics(num_words=4)
    for topic in topics:
        print(topic)
