from nltk.corpus import wordnet as wn

def getLemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

#print(getLemma('students'))
