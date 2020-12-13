import process_parameters as pp
import hashlib
import os
import sys
from os.path import isfile, join
from a_process_pdf import processPDF
from pathlib import Path
sys.path.append('../commons/')
from stop_words import getStopWords
from english_words import getEnglishWords
from md5_utils import md5

stopWords = getStopWords('../commons/stop_words')
englishWords = getEnglishWords('../commons/english_words')

def filesList():
    return list(Path(pp.PDF_FILES_PATH).rglob("*.[pP][dD][fF]"))
        
for file in filesList():
    metadataPath = pp.MODEL_FILE_PATH+'/'+md5(file)+'.metadata'
    if os.path.exists(metadataPath) and pp.KEEP_EXISTING_MODELS:
        print('Already Processed: '+file.stem)
        continue
    print('Start processing: '+file.stem)
    try:
        processPDF(file, stopWords, englishWords, pp.TOPICS_NUMBER, pp.WORDS_NUMBER, pp.PASSES_COUNT, pp.MODEL_FILE_PATH, False)
    except:
        print('Error Processing: '+file.stem)
    #break
