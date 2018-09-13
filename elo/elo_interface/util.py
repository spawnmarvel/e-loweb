import re
from elo_interface import stop_words

stop_list = stop_words.stopwords

def wordsToDict(words):
    freq = [words.count(w) for w in words]
    return dict(zip(words, freq))    

def wordsFreqSort(words):
    aux = [(words[key], key) for key in words]
    aux.sort()
    aux.reverse()
    return aux

def removeStop(words):
    global stop_list
    return[w for w in words if w not in stop_list]

	
def stripNonAlphaNum(text):
    return re.compile(r'\W+', re.UNICODE).split(text)

