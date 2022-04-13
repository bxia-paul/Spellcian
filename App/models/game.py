from App.database import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    word = db.Column(db.String(80), nullable=False)
    correct = db.Column(db.Boolean, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, word):
        self.word = word
        self.correct = False
        self.score = 0

    def toDict(self):
      return {
          "id": self.id,
          "word": self.word,
          "correct": self.correct,
          "score": self.score,
      }

    #To String method
    def __repr__(self):
      return self.word
