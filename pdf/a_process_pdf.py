import sys
sys.path.append('../commons/')
from get_lemma import getLemma
from stop_words import getStopWords
from english_words import getEnglishWords

from md5_utils import md5

from tika import parser
from nltk.tokenize import word_tokenize
import gensim
from gensim import corpora
import pickle
import os
import json


def processPDF(pdfFilePath, stopWords, englishWords, numTopics, numWords, modelPasses, outputPath, isScanned):
    allText = parser.from_file(str(pdfFilePath))
    paragList = allText['content'].split('\n\n')

    count = 0
    #
    text_data = []
    non_english = []
    for text in paragList:
        count +=1    
        tokens = word_tokenize(text)
    
        # non_punctuation_tokens = [token for token in tokens if token.isalnum()]
        removed_stop_words = [w for w in tokens if not w.lower() in stopWords]

        english_words_page = [w for w in removed_stop_words if     w.lower() in englishWords]
        non_english_page   = [w for w in removed_stop_words if not w.lower() in englishWords]
        non_english.extend(non_english_page)
    
        ch_tokens = []
        for word in english_words_page:
            ch_tokens.append(getLemma(word))
    
        text_data.append(ch_tokens)
        #break

    filename = md5(pdfFilePath)
    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    pickle.dump(corpus, open(outputPath+'/'+filename+'_corpus.pkl', 'wb'))
    dictionary.save(outputPath+'/'+filename+'_dict.gensim')


    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = numTopics, id2word=dictionary, passes=modelPasses)
    ldamodel.save(outputPath+'/'+filename+'_model5.gensim')
    topics = ldamodel.print_topics(num_words=numWords)
    # for topic in topics:
        # print(topic)

    base=os.path.basename(pdfFilePath)
    title = os.path.splitext(base)[0]
    metadata = {}
    metadata['title'] = title
    # metadata['isScanned'] = isScanned
    metadata['md5'] = filename
    metaFile = open(outputPath+'/'+filename+'.metadata', "w")
    metaFile.write(json.dumps(metadata))
    metaFile.close()
    #
    excludedFile = open(outputPath+'/'+filename+'.excluded', "w")
    excludedFile.write(json.dumps(non_english))
    excludedFile.close()

    print('Processed: '+filename+'::'+title)

########

# stop_words = getStopWords('../commons/stop_words')
# english_words = getEnglishWords('../commons/english_words')
# # file = 'files/Python 3 Text Processing with NLTK 3 Cookbook.pdf'
# # file = 'files/The Creation Account in Genesis 1:1-3 Part IV: The Theology of Genesis 1.pdf'
# file = 'files/6 Lessons Learned From Hundreds of Mobile Development Projects - Business Intelligence Info.pdf'
# processPDF(file, stop_words, english_words, 20, 4, 15, '../models', False)
