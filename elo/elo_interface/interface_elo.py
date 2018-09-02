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
        noun = []
        for np in blob.noun_phrases:
            noun.append(np)

        return "TextBlob: " + format(noun)