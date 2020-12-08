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
    if file.endswith(".diff"):
        list.append(file)

linkCount = 0

visualFilePath = '../visual/origin.js'
vf = open(visualFilePath, 'r')
line = vf.readline().replace('var dependencies =','')

obj = json.loads(line)

for linkFile in list:
    lf = open(folderName+'/'+linkFile, 'r')
    lt = lf.readline()
    linkMin = json.loads(lt)
    obj['links'].append(linkMin)

obj['links_count'] = len(list)

visualFilePath = '../visual/origin.js'
if os.path.exists(visualFilePath):
    os.remove(visualFilePath)

vf = open(visualFilePath, 'w')
vf.write('var dependencies =' + json.dumps(obj))
vf.close()
