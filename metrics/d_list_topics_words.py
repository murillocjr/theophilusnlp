from os import listdir
from os.path import isfile, join
import os
from nltk.corpus import words
import gensim
from gensim import corpora, models
import pickle
import json

folderName = '../models'

def filesList():
    return [f for f in listdir(folderName) if isfile(join(folderName, f))]

# if os.path.exists('topic_words.txt'):
    # os.remove('topic_words.txt')
    
# allWords = open('topic_words.txt', "w")

for file in filesList():
    if file.endswith("_model5.gensim"):
        metaFile = folderName + '/' + file[0: -14]+'.metadata'
        with open(metaFile) as json_file: 
            data = json.load(json_file)
            print('---' + data['md5'] +':'+ data['title'])

        ldamodel =  models.LdaModel.load(folderName +'/'+ file)
        # print(ldamodel.print_topics())
        for topic in ldamodel.print_topics():
            topicWords = topic[1].split('+')
            strLine = ''
            for wordPart in topicWords:
                topicWord = wordPart.strip()[7:-1]
                strLine = strLine + ',' + topicWord
                # if not topicWord in words.words():
                    # allWords.write(topicWord+"\n")
            print(strLine)
            

        # break
# allWords.close()
