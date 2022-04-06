from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(80), nullable=False, unique=True)
    email =  db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    lives = 3
    highscore = 0
    score = 0
    

    def __init__(self, username, email, password, lives, highscore, score):
        self.username = username
        self.email = email
        self.set_password(password)
        self.lives = lives
        self.highscore = highscore
        self.score = score

    def toDict(self):
        return{
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'highscore': self.highscore,
            'lives': self.lives    
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

