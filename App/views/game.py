from App.controllers import(
    getWordList
)

from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from gtts import gTTS

game_views = Blueprint('game_views', __name__, template_folder='../templates')

# start a new game


@game_views.route('/loadGame', methods=['POST'])
def game_page():
    result = request.form.get('gameChoice')
    word = getWordList(result)
    language = 'en'
    output = gTTS(text=word, lang=language, slow=False)
    output.save("App/static/speech.mp3")

    #playsound("speech.mp3")
    return render_template("game.html", result=result, word=word, sound=output)


