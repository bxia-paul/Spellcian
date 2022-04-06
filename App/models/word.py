from App.database import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wordname = db.Column(db.String(80), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    given = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, wordname, difficulty):
        self.wordname = wordname
        self.difficulty = difficulty
        self.given = False

    def toDict(self):
      return {
        "id": self.id,
        "wordname": self.wordname,
        "difficulty": self.difficulty,
        "given": self.given,
      }
    
    #To String method
    def __repr__(self):
      return '<Word {}>'.format(self.wordname)


