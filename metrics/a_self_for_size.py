import sys
sys.path.append('../commons/')
from model_utils import getTopicsFromModel
from os import listdir
from os.path import isfile, join
import os
from nltk.corpus import words
import gensim
from gensim import corpora, models
import pickle
import json

keepExisting = True
folderName = '../models'

def filesList():
    return [f for f in listdir(folderName) if isfile(join(folderName, f))]


for file in filesList():
    if file.endswith("_model5.gensim"):
        metaFile = folderName + '/' + file[0: -14]+'.metadata'
        if keepExisting:
            with open(metaFile) as json_file: 
                data = json.load(json_file)
                if ('size' in data) and ('topics' in data):
                    print('Already Processed: '+file[0: -14]+'::'+data['title'])
                    continue
    
        ldamodel =  models.LdaModel.load(folderName +'/'+ file)
        mdiff, annotation = ldamodel.diff(ldamodel, distance='jaccard', num_words=50)

        minimum = 2
        for row in mdiff:
            for val in row:
                if val>0:
                    if val < minimum:
                        minimum = val
                    
        if minimum == 2:
            size = 1
        else:
            size = round(40*(1-minimum))
        #
        ##
        topics = getTopicsFromModel(ldamodel)
        stringTopics = ''
        for topic in topics:
            for word in topic:
                stringTopics = stringTopics + word + ','
            stringTopics = stringTopics + '|'
        ##
        
        with open(metaFile) as json_file: 
            data = json.load(json_file)
            data['size'] = size
            data['topics'] = stringTopics
        

        mf = open(metaFile, 'w')
        json.dump(data, mf)
        mf.close()
        # break
