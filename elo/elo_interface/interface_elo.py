from datetime import datetime
from textblob import TextBlob

""" Elo is the interface to all functions, a controller. 
    Elo must be generic, since it will be used in Django, only MyCommand will be replaced in Django

"""

class Elo():

    def __init__(self):
        self.name = "e-lo"
        today = datetime.now()
        tmp_born = "2018-07-19 17:57"
        born = datetime.strptime(tmp_born, "%Y-%m-%d %H:%M")
        self.age = today - born
        self.response = None
        self.version = 1.1

    # implemented
    def __repr__(self):
        return repr("<Elo name:" +self.name)
    # implemented
    def toString(self):
        return format(self.name) + ". Age " + format(self.age) + ". V" + format(self.version)

    def text_summary(self, args):
        txt = args
        blob = TextBlob(txt)
        nouns = set()
        for word, tag in blob.tags:
            if tag == "NN":
                nouns.add(word.lemmatize())
        plural = set()
        for n in nouns:
             plural.add(n.pluralize())

        return format(plural)

    def text_insert(self, args):
        txt = args
        words_len = 0
        msg = ""
        summary = ""
        try:
            cont = txt.split(".")
            sentence_len = len(cont) - 1
            for i, v in enumerate(cont):
                x =  v.replace('"', '')
                msg += x
                # need to add back ., since we splitt on it...
                msg += "."
            word = msg.split(" ")
            words_len = len(word)
        except UnicodeDecodeError as uce:
            msg = format(uce)
        except Exception as ex:
            msg = format(ex)
        #remove the last - we added
        rm_last = len(msg)
        msg = msg[:rm_last - 1]
        tu = (msg, sentence_len, words_len)
        return tu


