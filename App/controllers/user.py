from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask_login import current_user

def get_all_users():
    return User.query.all()

def create_user(uname, mail, pord):
    try:
        newuser = User(username=uname, email=mail, password=pord)
        
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except IntegrityError: # attempted to insert a duplicate user based on e-mail
        db.session.rollback()
        return None

def set_level(difficulty):
    user = User.query.filter_by(id=current_user.id).first()
    try:
        user.level=difficulty
        db.session.add(user)
        db.session.commit()
        return user.toDict()
    except:
        db.session.rollback()
        return None

def reset_lives():
    user = User.query.filter_by(id=current_user.id).first()
    try:
        user.lives = 3
        db.session.add(user)
        db.session.commit()
        return user.toDict()
    except:
        db.session.rollback()
        return None

def update_lives():
    user = User.query.filter_by(id=current_user.id).first()
    try:
        user.lives = user.lives - 1
        db.session.add(user)
        db.session.commit()
        return user.toDict()
    except:
        db.session.rollback()
        return None

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def get_all_users():
    return User.query.all()