from sqlalchemy import true
from App.models import Word
from App.database import db

import csv
import random


def loadWords():
   word_file = csv.DictReader(
       open("App/spellican_word_list.csv", encoding='utf-8-sig'))
   for w in word_file:  # creates an object from the Word model
    db.session.add(Word(
        wordname=w["word"],
        difficulty=w["difficulity"]
    ))
    db.session.commit()

#randomly selects a word from easy list
def getWordList():
    wList = random.choice(Word.query.filter_by(
        difficulty=1, given=False).all())
    used = usedWord(wList.wordname)
    return wList.__repr__()

#randomly selects a word from medium list
def getMedWordList():
    wList = random.choice(Word.query.filter_by(
        difficulty=2, given=False).all())
    used = usedWord(wList.wordname)
    return wList.__repr__()

#randomly selects a word from hard list
def getHardWordList():
    wList = random.choice(Word.query.filter_by(
        difficulty=3, given=False).all())
    used = usedWord(wList.wordname)

    print(used.toDict())
    return wList.__repr__()


#set word to given = True


def usedWord(word):
    uWord = Word.query.filter_by(wordname=word).first()
    print(uWord.toDict())
    if uWord is None:
        return None

    try:
        uWord.given = True
        db.session.add(uWord)
        db.session.commit()
        return uWord
    except Exception as e:
        db.session.rollback()
        return None
