import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import gensim
from gensim import corpora, models
import pickle


def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

stop_words = set(stopwords.words('english'))

text_data = []


filename = 'Waltke-Cosmogony-BSac'
#filename = 'A_Manual_of_the_Book_of_Psalms'

NUM_TOPICS = 5
pdfFileObj = open(filename+'.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""

ldamodel =  models.LdaModel.load('../bible/model5.gensim')
dictionary = gensim.corpora.Dictionary.load('../bible/dictionary.gensim')

print(ldamodel.print_topics())

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

    if text != "":
       text = text
    else:
       text = textract.process(fileurl, method='tesseract', language='eng')

    tokens = word_tokenize(text)

    non_punctuation_tokens = [token for token in tokens if token.isalnum()]
    removed_stop_words = [w for w in non_punctuation_tokens if not w.lower() in stop_words] 

    ch_tokens = []
    for word in removed_stop_words:
        ch_tokens.append(get_lemma(word))

    new_doc_bow = dictionary.doc2bow(ch_tokens)

    print(ldamodel.get_document_topics(new_doc_bow))
