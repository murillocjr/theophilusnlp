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
import process_parameters as pp

def filesList():
    return [f for f in listdir(pp.MODEL_FILE_PATH) if isfile(join(pp.MODEL_FILE_PATH, f))]


for file in filesList():
    if file.endswith("_model5.gensim"):
        metaFile = pp.MODEL_FILE_PATH + '/' + file[0: -14]+'.metadata'
        if pp.KEEP_EXISTING_SIZE_TOPICS:
            with open(metaFile) as json_file: 
                data = json.load(json_file)
                if ('size' in data) and ('topics' in data):
                    print('Already Processed: '+file[0: -14]+'::'+data['title'])
                    continue
    
        ldamodel =  models.LdaModel.load(pp.MODEL_FILE_PATH +'/'+ file)
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
                stringTopics = stringTopics + word + '<br>'
            stringTopics = stringTopics + '<hr>'
        ##
        
        with open(metaFile) as json_file: 
            data = json.load(json_file)
            data['size'] = size
            data['topics'] = stringTopics
        

        mf = open(metaFile, 'w')
        json.dump(data, mf)
        mf.close()
        # break
