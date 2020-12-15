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

dependencies = {}
dependencies['objects']={}
dependencies['links']=[]
dependencies['links_count']=0
for file in filesList():
    if file.endswith(".metadata"):
        with open(pp.MODEL_FILE_PATH + '/' + file) as json_file: 
            data = json.load(json_file)
            dependencies['objects'][data['md5']]={
                'type': 'unknown', 
                'size': data['size'], 
                'title': data['title'],
                'topics': data['topics']
                }

visualFilePath = '../visual/origin.js'
if os.path.exists(visualFilePath):
    os.remove(visualFilePath)

vf = open(visualFilePath, 'w')
vf.write('var dependencies =' + json.dumps(dependencies))
vf.close()

