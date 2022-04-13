from App.controllers.user import reset_lives, update_lives
from App.models import Game
from App.database import db
from gtts import gTTS
from sqlalchemy.sql import func
from sqlalchemy import delete

def initGame():
    try:
        reset_lives()
        game = Game.query.all()
        db.session.delete(game)
        db.session.commit()
    except Exception as e:
        db.session.rollback()

def deleteLast():
    last = Game.query.order_by(Game.id.desc()).first()
    try:
        db.session.query(Game).filter_by(id=last.id).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()

def generateWord(word):
    language = 'en'
    output = gTTS(text=word, lang=language, slow=False)
    output.save("App/static/speech.mp3")

def addWord(word):
    try:
        db.session.add(Game(word))
        db.session.commit()
    except Exception as e:
        db.session.rollback()


def checkAnswer(guess):
    found = Game.query.order_by(Game.id.desc()).first()
    # return found.__repr__()
    if guess.lower() == found.__repr__().lower():
        score = Game.query.filter_by(word=found.__repr__()).first()
        try:
            score.score = 10
            score.correct = True
            db.session.add(score)
            db.session.commit()
            return 'Correct Spelling'
        except:
            db.session.rollback()
            return None
        # return  'Correct Spelling'
    else:
        update_lives()
        return 'Incorrect Spelling'


def totalScore():
    sum = db.session.query(func.sum(Game.score)).scalar()
    return sum

def endGame():
    end = Game.query.filter_by(id=6).first()
    
    if end is None:
        return None
    else:
        return 'End'    

def getGame():
    game = Game.query.all()
    return game
