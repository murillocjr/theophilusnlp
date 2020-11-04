import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import gensim
from gensim import corpora
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

text_data = []
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

    text_data.append(ch_tokens)
    
#    break

dictionary = corpora.Dictionary(text_data)
corpus = [dictionary.doc2bow(text) for text in text_data]
pickle.dump(corpus, open(filename+'_corpus.pkl', 'wb'))
dictionary.save(filename+'_dict.gensim')


ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
ldamodel.save(filename+'_model5.gensim')
topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)
