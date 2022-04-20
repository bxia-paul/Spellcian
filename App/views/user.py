from flask import Blueprint, redirect, render_template, jsonify, request, send_from_directory, url_for
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from flask_jwt import jwt_required

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    log_user,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/', methods=['GET'])
def index():
  return render_template('login.html')

# SIGNUP/REGISTER USERS
@user_views.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@user_views.route('/signup', methods=['POST'])
def signupAction():
    data = request.form
    user = create_user(data['username'], data['email'], data['password'], lives=3, highscore=0, score=0)
    if user != None:
        return redirect(url_for('user_views.homepage'))
    return render_template('signup.html')

@user_views.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@user_views.route('/login', methods=['POST'])
def loginAction():
    data = request.form
    user = log_user(data['username'], data['password'])
    if user != None:
        return redirect(url_for('user_views.homepage'))
    return render_template('home.html') #Redirects to home page

@user_views.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('user_views.login')) 


@user_views.route('/homepage', methods=['GET'])
@login_required
def homepage():
    return render_template('main-page.html')

#create a user
# @user_views.route('/register', methods=['POST'])
# def create_user():
#     data = request.get_json()
    
#     newuser = create_user(data['username'], data['email'], data['password'])

#     return (jsonify({"message":"created"}), 201) if newuser else (jsonify({"message":"could not create"}), 500)

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
