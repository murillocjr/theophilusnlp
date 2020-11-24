from os import listdir
from os.path import isfile, join

def getEnglishWords(txtPath):
    all_words = {}
    onlyfiles = [f for f in listdir(txtPath) if isfile(join(txtPath, f))]
    for file in onlyfiles:
        with open(txtPath+'/'+file) as f:
            e_words = f.readlines()
        e_words = [x.strip() for x in e_words]
        for ww in e_words:
            all_words[ww] = 1
    return all_words
    
# print(len(getEnglishWords('english_words')))
# if 'cat' in getEnglishWords('english_words'):
#     print('cat')
