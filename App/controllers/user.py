from App.models import User
from App.database import db


def get_all_users():
    return User.query.all()

def create_user(uname, mail, pord):
    return uname
    try:
        newuser = User(username=username, email=email, password=password)
        
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