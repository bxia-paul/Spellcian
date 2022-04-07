from App.models import Word
from App.database import db
import csv
import random

def loadWords():
   word_file = csv.DictReader(open("/workspace/Spellcian/App/spellican_word_list.csv", encoding='utf-8-sig'))
   
   for w in word_file: # creates an object from the Word model
    db.session.add(Word(
      wordname = w["word"],
      difficulty = w["difficulty"]
      ))
    db.session.commit()    

def getWordList(difficulty):
    wList = random.choice(Word.query.filter_by(difficulty=difficulty).all())
    return wList.__repr__()
    

