from flask import Blueprint, render_template, jsonify, request, send_from_directory, url_for, redirect
from flask_jwt import jwt_required
from flask_login import login_required

from App.models import User
from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    set_level,
    initGame
)
from App.views.game import(game_page)

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

#returns all users
@user_views.route('/allusers', methods=['GET'])
def get_todos():
  users = User.query.all()
  users_list = [ user.toDict() for user in users ] # convert user objects to list of dictionaries
  return jsonify({ "num_users": len(users_list), "users": users_list })

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json() 
    return jsonify(users)


@user_views.route('/level', methods=['GET'])
@login_required
def user_difficulty():
    return render_template("newgame.html")

#edits users difficulty    
@user_views.route('/level', methods=['POST'])
@login_required
def set_user_difficulty():
    result = request.form.get('gameChoice')
    set = set_level(result)
    initGame()
    return redirect(url_for('game_views.game_page'))

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')
