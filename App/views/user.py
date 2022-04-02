from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.models import User
from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

#create a user
@user_views.route('/register', methods=['POST'])
def create_user_page():
    data = request.get_json() 
    newuser = create_user(data['username'], data['email'], data['password'])
    return (jsonify({"message":"created"}), 201) if newuser else (jsonify({"message":"could not create"}), 500)

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/allusers', methods=['GET'])
def get_todos():
  users = User.query.all()
  users_list = [ user.toDict() for user in users ] # convert user objects to list of dictionaries
  return jsonify({ "num_users": len(users_list), "users": users_list })

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')
