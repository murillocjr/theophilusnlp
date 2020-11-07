from os import listdir
from os.path import isfile, join


def getStopWords():
    all_words = []
    onlyfiles = [f for f in listdir('stopwords') if isfile(join('stopwords', f))]
    for file in onlyfiles:
        with open('stopwords/'+file) as f:
            stop_words = f.readlines()
        stop_words = [x.strip() for x in stop_words]
        all_words.extend(stop_words)

    # print(len(all_words))
    all_words = list(dict.fromkeys(all_words))
    # print(len(all_words))
    return all_words
    

# print(len(getStopWords()))


