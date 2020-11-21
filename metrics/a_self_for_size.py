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


for file in filesList():
    if file.endswith("_model5.gensim"):
        ldamodel =  models.LdaModel.load(folderName +'/'+ file)
        mdiff, annotation = ldamodel.diff(ldamodel, distance='jaccard', num_words=50)

        totalVal = 0
        totalCount = 0

        for row in mdiff:
            for val in row:
                if val>0:
                    totalVal += val
                    totalCount += 1

        if totalCount>0:
            size = round(30*totalVal/totalCount)
        else:
            size = 1
        #
        metaFile = folderName + '/' + file[0: -14]+'.metadata'
        with open(metaFile) as json_file: 
            data = json.load(json_file)
            data['size'] = size
        
        # print(data)
        if os.path.exists('topic_words.txt'):
            os.remove('topic_words.txt')

        mf = open(metaFile, 'w')
        json.dump(data, mf)
        mf.close()
        # break
