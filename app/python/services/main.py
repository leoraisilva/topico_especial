from flask import Flask, request

from python.services.request import tabelas

app = Flask(__name__)

@app.route("/brasileirao-A")
def get_brasileiraoA():
    id = request.args.get('id')
    tabela = tabelas(int(id))
    return tabela.brasileiraoA()

@app.route("/brasileirao-B")
def get_brasileiraoB():
    id = request.args.get('id')
    tabela = tabelas(int(id))
    return tabela.brasileiraoB()

@app.route("/premier-league")
def get_ingles():
    id = request.args.get('id')
    tabela = tabelas(int(id))
    return tabela.ingles()

@app.route("/la-liga")
def get_espanhol():
    id = request.args.get('id')
    tabela = tabelas(int(id))
    return tabela.espanhol()

@app.route("/le-ligue-1")
def get_frances():
    id = request.args.get('id')
    tabela = tabelas(int(id))
    return tabela.frances()

@app.route("/bundesliga")
def get_alemao():
    id = request.args.get('id')
    tabela = tabelas(int(id))
    return tabela.alemao()

@app.route("/serie-A")
def get_italiano():
    id = request.args.get('id')
    tabela = tabelas(int(id))
    return tabela.italiano()

@app.route("/saudita")
def get_saudito():
    id = request.args.get('id')
    tabela = tabelas(int(id))
    return tabela.saudito()