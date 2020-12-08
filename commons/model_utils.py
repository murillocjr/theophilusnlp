from os import listdir
from os.path import isfile, join
import os
from nltk.corpus import words
import gensim
from gensim import corpora, models
import pickle
import json

def getTopicsFromModel(ldamodel):
    topics = []
    for topic in ldamodel.print_topics():
        topicWords = topic[1].split('+')
        topic = []
        for wordPart in topicWords:
            topicWord = wordPart.strip()[7:-1]
            topic.append(topicWord)
        topics.append(topic)
    return topics

###
# folderName = '../models'
# 
# def filesList():
    # return [f for f in listdir(folderName) if isfile(join(folderName, f))]
# 
# for file in filesList():
    # if file.endswith("_model5.gensim"):
        # ldamodel =  models.LdaModel.load(folderName+'/'+file)
        # print(getTopicsFromModel(ldamodel))
        # break
        
