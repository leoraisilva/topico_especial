from flask import Flask, request
from flask_cors import CORS

from .firebase import Firebase
from ..services.request import Football

app = Flask(__name__)

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route('/api/v1/brasileirao/')
def index_brasileirao_a():
    football = Football()
    return football.brasileiro_a()


@app.route('/api/v1/brasileirao/<posicao>')
def show_brasileirao_a(posicao):
    football = Football()
    return football.posicao_brasileiro_a(int(posicao) - 1)


@app.route('/api/v1/brasileirao-serie-b/')
def index_brasileirao_b():
    football = Football()
    return football.brasileiro_b()


@app.route('/api/v1/brasileirao-serie-b/<posicao>')
def show_brasileirao_b(posicao):
    football = Football()
    return football.posicao_brasileiro_b(int(posicao) - 1)


@app.route('/api/v1/premier-league/')
def index_premier_league():
    football = Football()
    return football.ingles()


@app.route('/api/v1/premier-league/<posicao>')
def show_premier_league(posicao):
    football = Football()
    return football.posicao_ingles(int(posicao) - 1)


@app.route('/api/v1/la-liga/')
def index_la_liga():
    football = Football()
    return football.espanhol()


@app.route('/api/v1/la-liga/<posicao>')
def show_la_liga(posicao):
    football = Football()
    return football.posicao_espanhol(int(posicao) - 1)


@app.route('/api/v1/bundesliga/')
def index_bundesliga():
    football = Football()
    return football.alemao()


@app.route('/api/v1/bundesliga/<posicao>')
def show_bundesliga(posicao):
    football = Football()
    return football.posicao_alemao(int(posicao) - 1)


@app.route('/api/v1/league-one/')
def index_league_one():
    football = Football()
    return football.frances()


@app.route('/api/v1/league-one/<posicao>')
def show_league_one(posicao):
    football = Football()
    return football.posicao_frances(int(posicao) - 1)


@app.route('/api/v1/serie-a/')
def index_serie_a():
    football = Football()
    return football.italiano()


@app.route('/api/v1/serie-a/<posicao>')
def show_serie_a(posicao):
    football = Football()
    return football.posicao_italiano(int(posicao) - 1)


@app.route('/api/v1/saudita/')
def index_saudita():
    football = Football()
    return football.saudita()


@app.route('/api/v1/saudita/<posicao>')
def show_saudita(posicao):
    football = Football()
    return football.posicao_saudita(int(posicao) - 1)


@app.route('/api/v1/jogos/brasileirao/')
def jogos_brasileirao():
    football = Football()
    return football.games_brasileirao()


@app.route('/api/v1/jogos/brasileirao-serie-b/')
def jogos_brasileirao_b():
    football = Football()
    return football.games_brasileiraoB()

@app.route('/api/v1/jogos/premier-league/')
def jogos_ingles():
    football = Football()
    return football.games_ingles()

@app.route('/api/v1/jogos/la-liga/')
def jogos_espanhol():
    football = Football()
    return football.games_espanhol()

@app.route('/api/v1/jogos/bundesliga/')
def jogos_alemao():
    football = Football()
    return football.games_alemao()

@app.route('/api/v1/jogos/league-one/')
def jogos_frances():
    football = Football()
    return football.games_frances()

@app.route('/api/v1/jogos/serie-a/')
def jogos_italiano():
    football = Football()
    return football.games_italiano()

@app.route('/api/v1/jogos/saudita/')
def jogos_saudita():
    football = Football()
    return football.games_saudita()

@app.route('/api/v1/ultimos/brasileirao/<time>/<adversario>')
def ultimos_brasileirao(time, adversario):
    firebase = Firebase()
    return firebase.ultimo_jogo(time, adversario)
