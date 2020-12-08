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

list = []
for file in filesList():
    if file.endswith("_model5.gensim"):
        list.append(file[0: -14])

for i in range(0, len(list)):
    for j in range(i+1, len(list)):
        diffFile = folderName+'/'+list[i]+'_'+list[j]+'.diff'            
        if os.path.exists(diffFile) and keepExisting:
            print('Already Processed: '+list[i]+'_'+list[j])
            continue

        print('Processing: '+list[i]+'_'+list[j])
        lda_fst =  models.LdaModel.load(folderName+'/'+list[i]+'_model5.gensim')
        lda_snd =  models.LdaModel.load(folderName+'/'+list[j]+'_model5.gensim')

        mdiff, annotation = lda_fst.diff(lda_snd, distance='jaccard', num_words=50)
# 
        minimum = 2
        for row in mdiff:
            for val in row:
                if val > 0:
                    if val < minimum:
                        minimum = val

        linkMin = {'source': list[i], 'dest': list[j], 'distance': minimum}

        df = open(diffFile, 'w')
        df.write(json.dumps(linkMin))
        df.close()
