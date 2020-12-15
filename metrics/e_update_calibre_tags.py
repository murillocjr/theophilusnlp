import process_parameters as pp
from pathlib import Path
# 
# import hashlib
import os
import xml.etree.ElementTree as ET

import sys
# from os.path import isfile, join
# from a_process_pdf import processPDF
sys.path.append('../commons/')
# from stop_words import getStopWords
# from english_words import getEnglishWords
from md5_utils import md5
import json

def filesList():
    return list(Path(pp.PDF_FILES_PATH).rglob("*.[pP][dD][fF]"))
        
for file in filesList():
    #getting topics
    modelMetadata = pp.MODEL_FILE_PATH +'/'+ md5(file)+'.metadata'
    with open(modelMetadata) as json_file: 
        data = json.load(json_file)
        print(data['topics'])

    

    
    # metadataPath = str(file.parents[0])+'/metadata.opf'
    # print(metadataPath)
    # if os.path.exists(metadataPath):
        # tree = ET.parse(metadataPath)
        # root = tree.getroot()
        # for elem in root:
            # if 'metadata' in  elem.tag:
                # # print(elem.tag)
                # newTag = ET.SubElement(elem,'dc:subject')
                # newTag.text = 'sampleTag'
                # for subelem in elem:
                    # if 'subject' in subelem.tag:
                        # print(subelem)
        # tree.write(metadataP)

        
    # print('Start processing: '+file.stem)
    # try:
        # processPDF(file, stopWords, englishWords, pp.TOPICS_NUMBER, pp.WORDS_NUMBER, pp.PASSES_COUNT, pp.MODEL_FILE_PATH, False)
    # except:
        # print('Error Processing: '+file.stem)
    break



# import sys
# sys.path.append('../commons/')
# from model_utils import getTopicsFromModel
# from os import listdir
# from os.path import isfile, join
# import os
# from nltk.corpus import words
# import gensim
# from gensim import corpora, models
# import pickle
# import json
# 
# keepExisting = True
# folderName = '../models'
# 
# PDF_FILES_PATH = '/home/ubuntu/Calibre Library'
# 
# 
# def filesList():
    # return [f for f in listdir(folderName) if isfile(join(folderName, f))]
# 
# 
# for file in filesList():
    # if file.endswith("_model5.gensim"):
        # metaFile = folderName + '/' + file[0: -14]+'.metadata'
        # if keepExisting:
            # with open(metaFile) as json_file:
                # data = json.load(json_file)
                # if ('size' in data) and ('topics' in data):
                    # print('Already Processed: '+file[0: -14]+'::'+data['title'])
                    # continue
    # 
        # ldamodel =  models.LdaModel.load(folderName +'/'+ file)
        # mdiff, annotation = ldamodel.diff(ldamodel, distance='jaccard', num_words=50)
# 
        # minimum = 2
        # for row in mdiff:
            # for val in row:
                # if val>0:
                    # if val < minimum:
                        # minimum = val
                    # 
        # if minimum == 2:
            # size = 1
        # else:
            # size = round(40*(1-minimum))
        # #
        # ##
        # topics = getTopicsFromModel(ldamodel)
        # stringTopics = ''
        # for topic in topics:
            # for word in topic:
                # stringTopics = stringTopics + word + '<br>'
            # stringTopics = stringTopics + '-::-<br>'
        # ##
        # 
        # with open(metaFile) as json_file:
            # data = json.load(json_file)
            # data['size'] = size
            # data['topics'] = stringTopics
        # 
# 
        # mf = open(metaFile, 'w')
        # json.dump(data, mf)
        # mf.close()
        # # break
