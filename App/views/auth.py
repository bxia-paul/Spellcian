from flask import Blueprint, flash, render_template, request, jsonify
from werkzeug.utils import redirect

auth_views = Blueprint("auth", __name__, template_folder='../templates')

@auth_views.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

 '''
@auth_views.route('/auth', methods=['POST'])
def login_action():
    fname = request.form['first_name']
    lname = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    res = create_user(email, password, fname, lname)
    if (res):
        flash('User Created')
        return redirect('/')
    else:
        flash("Email Taken")
        return redirect('/signup')  
   '''     
