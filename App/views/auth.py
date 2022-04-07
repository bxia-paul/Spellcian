from flask import Blueprint, flash, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import redirect
from App.models import User

from flask_login import LoginManager, current_user, login_user, login_required

from App.controllers import (
    authenticate,
    create_user
)

auth_views = Blueprint("auth", __name__, template_folder='../templates')

@auth_views.route("/login", methods=['GET'])
def login_page():
    return render_template("login.html")

@auth_views.route('/login', methods=['POST'])
def login():
    data = request.form
    user = User.query.filter_by(username = data['username']).first()
    if user and user.check_password(data['password']): # check credentials
      flash('Logged in successfully.') # send message to next page
      login_user(user) # login the user
      return render_template("newgame.html") # redirect to main page if login successful
    else:
      flash('Invalid username or password') # send message to next page
    return render_template("login.html") 

# SIGNUP/REGISTER USERS
@auth_views.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@auth_views.route('/signup', methods=['POST'])
def signupAction():
    data = request.form
    user = create_user(data['username'], data['email'], data['password'])
    if user != None:
        return redirect(url_for('user_views.client_app'))
    return render_template('login.html')    
      
