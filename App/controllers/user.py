from App.models import User
from App.database import db
from sqlalchemy.exc import IntegrityError

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
    
def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def get_all_users():
    return User.query.all()