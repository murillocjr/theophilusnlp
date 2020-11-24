from os import listdir
from os.path import isfile, join


def getStopWords(txtPath):
    all_words = {}
    onlyfiles = [f for f in listdir(txtPath) if isfile(join(txtPath, f))]
    for file in onlyfiles:
        with open(txtPath+'/'+file) as f:
            stop_words = f.readlines()
        stop_words = [x.strip() for x in stop_words]
        for ww in stop_words:
            all_words[ww] = 1

    return all_words
    
# print(len(getStopWords('stop_words')))
# if 'the' in getStopWords('stop_words'):
#     print('the')


