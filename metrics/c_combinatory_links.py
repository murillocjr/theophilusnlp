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

list = []
for file in filesList():
    if file.endswith("_model5.gensim"):
        list.append(file[0: -14])

linkCount = 0

visualFilePath = '../visual/origin.js'
vf = open(visualFilePath, 'r')
line = vf.readline().replace('var dependencies =','')

obj = json.loads(line)
# print(obj)

for i in range(0, len(list)):
    # minDis = 2
    # k = i
    # maxDis = 0
    # m = i
    for j in range(i+1, len(list)):
        # if i == j:
        #     continue

        lda_fst =  models.LdaModel.load('../models/'+list[i]+'_model5.gensim')
        lda_snd =  models.LdaModel.load('../models/'+list[j]+'_model5.gensim')

        mdiff, annotation = lda_fst.diff(lda_snd, distance='jaccard', num_words=50)

        #####
        minimum = 2
        for row in mdiff:
            for val in row:
                if val > 0:
                    if val < minimum:
                        minimum = val
                    
        # if minimum < minDis:
        #     k = j 
        #     distanceMin = round(500*(minimum))
        #     minDis = minimum

        #####
        # maximum = 0
        # for row in mdiff:
        #     for val in row:
        #         if val < 1:
        #             if val > maximum:
        #                 maximum = val
                    
        # if maximum > maxDis:
        #     m = j 
        #     distanceMax = round(500*(maximum))
        #     maxDis = maximum

        linkMin = {'source': list[i], 'dest': list[j], 'distance': round(500*(minimum))}
        obj['links'].append(linkMin)
        linkCount += 1

    # linkMax = {'source': list[i], 'dest': list[m], 'distance': distanceMax}
    # obj['links'].append(linkMax)
    # linkCount += 1
    

obj['links_count'] = linkCount

visualFilePath = '../visual/origin.js'
if os.path.exists(visualFilePath):
    os.remove(visualFilePath)

vf = open(visualFilePath, 'w')
vf.write('var dependencies =' + json.dumps(obj))
vf.close()
