from App.models import Word
from App.database import db
import csv

def loadWords():
   word_file = csv.DictReader(open("/workspace/Spellcian/App/spellican_word_list.csv", encoding='utf-8-sig'))
   
   for w in word_file: # creates an object from the Word model
    db.session.add(Word(
      wordname = w["word"],
      difficulty = w["difficulty"]
      ))
    db.session.commit()    

def getWordList():
    wList = Word.query.all()
    

