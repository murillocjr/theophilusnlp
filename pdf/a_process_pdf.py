import sys
sys.path.append('../commons/')
from get_lemma import getLemma
from stop_words import getStopWords
from md5_utils import md5

import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
import gensim
from gensim import corpora
import pickle
import os
import json


def processPDF(pdfFilePath, stopWords, numTopics, numWords, modelPasses, outputPath, isScanned):
    pdfFileObj = open(pdfFilePath,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    #
    text_data = []
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text = ""
        
        if (not isScanned):
           text = pageObj.extractText()
        else:
           text = textract.process(fileurl, method='tesseract', language='eng')

        encoded_string = text.encode("ascii", "ignore")
        text = encoded_string.decode()
    
        tokens = word_tokenize(text)
    
        non_punctuation_tokens = [token for token in tokens if token.isalnum()]
        removed_stop_words = [w for w in non_punctuation_tokens if not w.lower() in stopWords]
    
        ch_tokens = []
        for word in removed_stop_words:
            ch_tokens.append(getLemma(word))
    
        text_data.append(ch_tokens)
        
        # break

    filename = md5(pdfFilePath)
    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    pickle.dump(corpus, open(outputPath+'/'+filename+'_corpus.pkl', 'wb'))
    dictionary.save(outputPath+'/'+filename+'_dict.gensim')


    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = numTopics, id2word=dictionary, passes=modelPasses)
    ldamodel.save(outputPath+'/'+filename+'_model5.gensim')
    topics = ldamodel.print_topics(num_words=numWords)
    for topic in topics:
        print(topic)

    base=os.path.basename(pdfFilePath)
    title = os.path.splitext(base)[0]
    metadata = {}
    metadata['title'] = title
    metadata['isScanned'] = isScanned
    metadata['pagesCount'] = num_pages
    metadata['md5'] = filename
    metaFile = open(outputPath+'/'+filename+'.metadata', "w")
    metaFile.write(json.dumps(metadata))
    metaFile.close()

    print('Processed: '+title)    


# stop_words = getStopWords('../commons/stop_words')
# processPDF('files/The Creation Account in Genesis 1:1-3 Part IV: The Theology of Genesis 1.pdf', stop_words, 20, 4, 15, '../models', False)
