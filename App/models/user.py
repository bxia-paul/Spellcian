from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    email =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    lives = db.Column(db.Integer)
    highscore = db.Column(db.Integer)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)
        self.lives = 3
        self.highscore = 0

    def toDict(self):
        return{
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'lives': self.lives,
            'highscore': self.highscore
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

