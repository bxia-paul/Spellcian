from flask import Blueprint, flash, render_template, request, jsonify, redirect
from werkzeug.utils import redirect
from App.models import User

from flask_login import LoginManager, current_user, login_user, login_required

from App.controllers import (
    authenticate
)

auth_views = Blueprint("auth", __name__, template_folder='../templates')

@auth_views.route("/login", methods=['GET'])
def login_page():
    return render_template("login.html")

@auth_views.route('/login', methods=['POST'])
def login():
    data = request.form
    user = User.query.filter_by(email = data['email']).first()
    if user and user.check_password(data['password']): # check credentials
      flash('Logged in successfully.') # send message to next page
      login_user(user) # login the user
      return render_template("newgame.html") # redirect to main page if login successful
    else:
      flash('Invalid username or password') # send message to next page
    return render_template("login.html") 
      
