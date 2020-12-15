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
    lf = open(pp.MODEL_FILE_PATH+'/'+linkFile, 'r')
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
