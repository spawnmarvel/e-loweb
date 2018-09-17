import re
from elo_interface import stop_words

stop_list = stop_words.stopwords

def textToDict(words):
	freq = []
	for w in words:
	    freq.append(words.count(w))
	return dict(zip(words, freq))    

def textFreqSort(words):
	aux = []
	for k in words:
	    item = (words[k], k)
	    aux.append(item)
	aux.sort()
	aux.reverse()
	return aux

def removeStopWords(words):
    global stop_list
    result = []
    for w in words:
	    if w not in stop_list:
		    result.append(w)
			
    return result	

def stripNonAlphaNum(words):
    return re.compile(r'\W+', re.UNICODE).split(words)


def createIndex(words):
    tmp = stripNonAlphaNum(words)
    rm_stop = removeStopWords(tmp)
    to_dict = textToDict(rm_stop)
    index = textFreqSort(to_dict)
    return index

