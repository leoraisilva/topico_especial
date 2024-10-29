from flask import Flask, request
from flask_cors import CORS

from python.services.request import Tabela

app = Flask(__name__)

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.route('/api/v1/brasileirao/')
def index_brasileirao_a():
    return Tabela.brasileiro_a()

@app.route('/api/v1/brasileirao/<posicao>')
def show_brasileirao_a(posicao):
    return Tabela.posicao_brasileiro_a(int(posicao) - 1)

@app.route('/api/v1/brasileirao-serie-b/')
def index_brasileirao_b():
    return Tabela.brasileiro_b()

@app.route('/api/v1/brasileirao-serie-b/<posicao>')
def show_brasileirao_b(posicao):
    return Tabela.posicao_brasileiro_b(int(posicao) - 1)

@app.route('/api/v1/premier-league/')
def index_premier_league():
    return Tabela.ingles()

@app.route('/api/v1/premier-league/<posicao>')
def show_premier_league(posicao):
    return Tabela.posicao_ingles(int(posicao) - 1)

@app.route('/api/v1/la-liga/')
def index_la_liga():
    return Tabela.espanhol()

@app.route('/api/v1/la-liga/<posicao>')
def show_la_liga(posicao):
    return Tabela.posicao_espanhol(int(posicao) - 1)

@app.route('/api/v1/bundesliga/')
def index_bundesliga():
    return Tabela.alemao()

@app.route('/api/v1/bundesliga/<posicao>')
def show_bundesliga(posicao):
    return Tabela.posicao_alemao(int(posicao) - 1)

@app.route('/api/v1/league-one/')
def index_league_one():
    return Tabela.frances()

@app.route('/api/v1/league-one/<posicao>')
def show_league_one(posicao):
    return Tabela.posicao_frances(int(posicao) - 1)

@app.route('/api/v1/serie-a/')
def index_serie_a():
    return Tabela.italiano()

@app.route('/api/v1/serie-a/<posicao>')
def show_serie_a(posicao):
    return Tabela.posicao_italiano(int(posicao) - 1)

@app.route('/api/v1/saudita/')
def index_saudita():
    return Tabela.saudita()

@app.route('/api/v1/saudita/<posicao>')
def show_saudita(posicao):
    return Tabela.posicao_saudita(int(posicao) - 1)
