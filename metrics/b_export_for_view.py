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

dependencies = {}

dependencies['objects']={}
for file in filesList():
    if file.endswith(".metadata"):
        with open(folderName + '/' + file) as json_file: 
            data = json.load(json_file)
            dependencies['objects'][data['title']]={'type': 'unknown', 'size': data['size']}

visualFilePath = '../visual/origin.js'
if os.path.exists(visualFilePath):
    os.remove(visualFilePath)

vf = open(visualFilePath, 'w')
vf.write('var dependencies =' + json.dumps(dependencies))
vf.close()

