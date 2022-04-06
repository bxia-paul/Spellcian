from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask import flash

def get_all_users():
    return User.query.all()

def create_user(uname, mail, pword, lives, highscore, score):
    try:
        newuser = User(username=uname, email=mail, password=pword, lives=3, highscore=0, score=0)
        db.session.add(newuser)
        db.session.commit()
        flash('User created successfully.') # send message to next page
        login_user(newuser) # login the user
        return newuser
    except IntegrityError: # attempted to insert a duplicate user based on e-mail
        flash("username or email already exists") # error message
        db.session.rollback()
        return None

def log_user(uname, pword):
    user = User.query.filter_by(username = uname).first()
    if user and user.check_password(pword): # check credentials
        login_user(user) # login the user
        flash('Logged in successfully.') # send message to next page
        return user
    else:
        flash('Invalid username or password') # send message to next page
    return None

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def get_all_users():
    return User.query.all()