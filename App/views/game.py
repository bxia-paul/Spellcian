from flask import Blueprint, render_template, request
from flask_login import current_user,  login_required

from App.controllers import(
    getWordList,
    generateWord,
    addWord,
    checkAnswer,
    totalScore,
    endGame,
    getGame,
    deleteLast
)

game_views = Blueprint('game_views', __name__, template_folder='../templates')


@game_views.route('/newWord', methods=['POST'])
@login_required
def newWord(difficulty):
    word = getWordList(difficulty)
    addWord(word)
    generateWord(word)
    return word


@game_views.route('/loadGame', methods=['GET'])
@login_required
def game_page():
    word = newWord(current_user.level)
    generateWord(word)
    return render_template("game.html", word=word)


@game_views.route('/checkAnswer', methods=['POST'])
@login_required
def isCorrect():
    answer = request.form.get('guess')
    check = checkAnswer(answer)

    return render_template("test.html", answer=answer, x=check)


@game_views.route('/next', methods=['POST'])
@login_required
def nextWord():
    answer = request.form.get('guess')
    check = checkAnswer(answer)
    s = totalScore()

    word = getWordList(current_user.level)
    generateWord(word)
    addWord(word)
    end = endGame()

    if end != None or current_user.lives == 0:
        deleteLast()
        tgame = getGame()
        return render_template("endgame.html", game=tgame, total=s)
    else:
        return render_template("game.html",  word=word, status=check, score=s)
