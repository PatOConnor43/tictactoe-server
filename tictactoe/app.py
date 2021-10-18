from flask import Flask
import json
import base64
from enum import Enum

app = Flask(__name__)

class GameStates(Enum):
    PLAYER_WINS = 'PLAYER_WINS'
    COMPUTER_WINS = 'COMPUTER_WINS'
    DRAW = 'DRAW'
    PLAYING = 'PLAYING'


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/start")
def start_game():
    game = {}
    board = [[None, None, None], [None, None, None], [None, None, None]]
    state = GameStates.PLAYING
    game['board'] = board
    game['state'] = state.name
    json_game = json.dumps(game)
    identifier = base64.b64encode(json_game.encode('ascii')).decode('UTF-8')
    return json.dumps({'id': identifier, 'game': game})
