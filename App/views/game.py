from calendar import c
from flask import Blueprint, flash, redirect, render_template, request, send_from_directory, url_for
from flask_login import current_user

from App.models import db
from App.controllers import(
    getWordList,
    getMedWordList,
    getHardWordList,
    update_lives,
    update_highscore,
    reset_lives
)

game_views = Blueprint('game_views', __name__, template_folder='../templates')


@game_views.route('/', methods=['GET'])
def home():
    return render_template('login.html')

@game_views.route('/home', methods=['GET'])
def home_opts():
    return render_template("main-page.html")

@game_views.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')


@game_views.route('/lost_easy', methods=['GET'])
def lost_easy():
    return render_template('lost_easy.html')


@game_views.route('/win_easy', methods=['GET'])
def win_easy():
    return render_template('win_easy.html')


@game_views.route('/lost_medium', methods=['GET'])
def lost_medium():
    return render_template('lost_medium.html')


@game_views.route('/win_medium', methods=['GET'])
def win_medium():
    return render_template('win_medium.html')


@game_views.route('/lost_hard', methods=['GET'])
def lost_hard():
    return render_template('lost_hard.html')


@game_views.route('/win_hard', methods=['GET'])
def win_hard():
    return render_template('win_hard.html')

# MUST ADD LOGIN FEATURES AND REPLACE INSTANCES OF "bob" with the current_user


@game_views.route('/easy', methods=['GET', 'POST'])
def play_easy():
    global score

    bee_word = getWordList()
    message = ""
    gametype = "Easy"

    if request.method == 'GET':
        reset_lives()
        score = 0

    if request.method == 'POST':
        form = request.form
        user_spelling = form["spelling"]
        word_given = form["word"]
        print(user_spelling)
        print(word_given)
        if word_given == user_spelling:
            message = "Correct"
            score += 10
        else:
            message = "Wrong, try again!"
            score += 0
            update_lives()

            if current_user.lives == 0:
                if current_user.highscore < score:
                    update_highscore(score)
                return redirect(url_for("game_views.lost_easy"))
    return render_template("game2.html", message=message, gametype=gametype, score=score, word=bee_word)


@game_views.route('/medium', methods=['GET', 'POST'])
def play_medium():
    global score
    bee_word = getMedWordList()
    message = ""
    gametype = "Medium"

    if request.method == 'GET':
        reset_lives()
        score = 0

    if request.method == 'POST':
        form = request.form
        user_spelling = form["spelling"]
        word_given = form["word"]

        if word_given == user_spelling:
            message = "Correct"
            score += 10
        else:
            message = "Wrong, try again!"
            score += 0
            update_lives()

            if current_user.lives == 0:
                if current_user.highscore < score:
                    update_highscore(score)
                return redirect(url_for("game_views.lost_medium"))
    return render_template("game2.html", message=message, gametype=gametype, score=score, word=bee_word)


@game_views.route('/hard', methods=['GET', 'POST'])
def play_hard():
    global score
    bee_word = getHardWordList()
    message = ""
    gametype = "Hard"

    if request.method == 'GET':
        reset_lives()
        score = 0

    if request.method == 'POST':
        form = request.form
        user_spelling = form["spelling"]
        word_given = form["word"]

        if word_given == user_spelling:
            message = "Correct"
            score += 10
        else:
            message = "Wrong, try again!"
            score += 0
            update_lives()

            if current_user.lives == 0:
                if current_user.highscore < score:
                    update_highscore(score)
                return redirect(url_for("game_views.lost_hard"))
    return render_template("game2.html", message=message, gametype=gametype, score=score, word=bee_word)
