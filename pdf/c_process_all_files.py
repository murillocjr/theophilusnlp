from os import listdir
from os.path import isfile, join
from a_process_pdf import processPDF
import process_parameters as pp
import hashlib
import os

import sys
sys.path.append('../commons/')
from stop_words import getStopWords
from english_words import getEnglishWords

from md5_utils import md5

keepExisting = True
folderName = 'files'
stopWords = getStopWords('../commons/stop_words')
englishWords = getEnglishWords('../commons/english_words')

def filesList():
    return [f for f in listdir(folderName) if isfile(join(folderName, f))]
    
for file in filesList():
    metadataPath = '../models/'+md5(folderName+'/'+file)+'.metadata'
    if os.path.exists(metadataPath) and keepExisting:
        print('Already Processed: '+file)
        continue
    print('Start processing: '+file)
    processPDF(folderName+'/'+file, stopWords, englishWords, pp.TOPICS_NUMBER, pp.WORDS_NUMBER, pp.PASSES_COUNT, '../models', False)
    #break
