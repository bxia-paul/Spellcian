#from tkinter import scrolledtext
from flask import Blueprint, flash, redirect, render_template, request, send_from_directory, url_for
import random
#from gtts import gTTS
#import pyttsx3

from App.models.user import User
#engine = pyttsx3.init()

api_views = Blueprint('api_views', __name__, template_folder='../templates')

easy_words = ["dog"]
medium_words = ["israel"]
hard_words = ["perspicacity"]

bob = User("bobby", "bob@gmail.com", "bobpass", 3, 0, 0)
#score = 0

@api_views.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@api_views.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html', yhighscore = bob.highscore)

@api_views.route('/lost_easy', methods=['GET'])
def lost_easy():
    return render_template('lost_easy.html')

#def tts(word):
#    engine.say(word)
#    engine.runAndWait()
#    engine.endLoop()
#    engine.stop()

@api_views.route('/easy', methods = ['GET', 'POST'])
def play_easy():
    bee_word = random.choice(easy_words)
    #tts(bee_word)
    message = ""
    gametype = "Easy"
    #pyttsx3.speak(bee_word)
    if request.method == 'POST':
        form = request.form
        user_spelling = form["spelling"]
        if bee_word == user_spelling:
            message = "Correct"
            bob.score +=10
            #return render_template("game_over.html", message = message, score = bob.score, word = bee_word)
        else:
            message = "Wrong, try again!"
            bob.lives -= 1
        if bob.lives == 0:
            bob.lives = 3
            if bob.highscore < bob.score:
                bob.highscore = bob.score
            bob.score = 0
            return render_template("lost_easy.html")
    return render_template("game.html", message = message, gametype=gametype, score = bob.score, yhighscore = bob.highscore, word = bee_word)

@api_views.route('/medium', methods = ['GET', 'POST'])
def play_medium():
    bee_word = random.choice(medium_words)
    message = ""
    gametype = "Medium"
    if request.method == 'POST':
        form = request.form
        user_spelling = form["spelling"]
        if bee_word == user_spelling:
            message = "Correct"
            return render_template("game_over.html", message = message, gametype=gametype)
        else:
            message = "Wrong, try again!"
    return render_template("game.html", message = message, gametype=gametype)

@api_views.route('/hard', methods = ['GET', 'POST'])
def play_hard():
    bee_word = random.choice(hard_words)
    message = ""
    gametype = "Hard"
    if request.method == 'POST':
        form = request.form
        user_spelling = form["spelling"]
        if bee_word == user_spelling:
            message = "Correct"
            return render_template("game_over.html", message = message, gametype=gametype)
        else:
            message = "Wrong, try again!"
    return render_template("game.html", message = message, gametype=gametype)