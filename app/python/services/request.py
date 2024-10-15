import json
import re

import requests
from bs4 import BeautifulSoup


class tabelas:
    def __init__(self, id):
        self.id = id

    def brasileiraoA(self):
        if self.id < 0 & self.id >= 20:
            return "erro na requesicao"
        http_request = requests.get("https://ge.globo.com/futebol/brasileirao-serie-a/")
        soup = BeautifulSoup(http_request.content, "html.parser")
        resultado = soup.find('script', id='scriptReact')
        result = resultado.string
        constant = re.findall(r'const classificacao\s*=\s*(.*?);', result)
        obj = json.loads(constant[0])
        result = obj['classificacao']
        return result[self.id]


    def brasileiraoB(self):
        if self.id < 0 & self.id >= 20:
            return "erro na requesicao"
        http_request = requests.get("https://ge.globo.com/futebol/brasileirao-serie-b/")
        soup = BeautifulSoup(http_request.content, "html.parser")
        resultado = soup.find('script', id='scriptReact')
        result = resultado.string
        constant = re.findall(r'const classificacao\s*=\s*(.*?);', result)
        obj = json.loads(constant[0])
        result = obj['classificacao']
        return result[self.id]


    def ingles(self):
        if self.id < 0 & self.id >= 20:
            return "erro na requesicao"
        http_request = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-ingles/")
        soup = BeautifulSoup(http_request.content, "html.parser")
        resultado = soup.find('script', id='scriptReact')
        result = resultado.string
        constant = re.findall(r'const classificacao\s*=\s*(.*?)\n', result)
        constant = constant[0].rstrip(';')
        obj = json.loads(constant)
        result = obj['classificacao']
        return result[self.id]


    def espanhol(self):
        if self.id < 0 & self.id >= 20:
            return "erro na requesicao"
        http_request = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-espanhol/")
        soup = BeautifulSoup(http_request.content, "html.parser")
        resultado = soup.find('script', id='scriptReact')
        result = resultado.string
        constant = re.findall(r'const classificacao\s*=\s*(.*?)\n', result)
        constant = constant[0].rstrip(';')
        obj = json.loads(constant)
        result = obj['classificacao']
        return result[self.id]


    def italiano(self):
        if self.id < 0 & self.id >= 20:
            return "erro na requesicao"
        http_request = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-italiano/")
        soup = BeautifulSoup(http_request.content, "html.parser")
        resultado = soup.find('script', id='scriptReact')
        result = resultado.string
        constant = re.findall(r'const classificacao\s*=\s*(.*?)\n', result)
        constant = constant[0].rstrip(';')
        obj = json.loads(constant)
        result = obj['classificacao']
        return result[self.id]


    def alemao(self):
        if self.id < 0 & self.id >= 20:
            return "erro na requesicao"
        http_request = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-alemao/")
        soup = BeautifulSoup(http_request.content, "html.parser")
        resultado = soup.find('script', id='scriptReact')
        result = resultado.string
        constant = re.findall(r'const classificacao\s*=\s*(.*?)\n', result)
        constant = constant[0].rstrip(';')
        obj = json.loads(constant)
        result = obj['classificacao']
        return result[self.id]


    def frances(self):
        if self.id < 0 & self.id >= 20:
            return "erro na requesicao"
        http_request = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-frances/")
        soup = BeautifulSoup(http_request.content, "html.parser")
        resultado = soup.find('script', id='scriptReact')
        result = resultado.string
        constant = re.findall(r'const classificacao\s*=\s*(.*?)\n', result)
        constant = constant[0].rstrip(';')
        obj = json.loads(constant)
        result = obj['classificacao']
        return result[self.id]


    def saudito(self):
        if self.id < 0 & self.id >= 20:
            return "erro na requesicao"
        http_request = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-saudita/")
        soup = BeautifulSoup(http_request.content, "html.parser")
        resultado = soup.find('script', id='scriptReact')
        result = resultado.string
        constant = re.findall(r'const classificacao\s*=\s*(.*?)\n', result)
        constant = constant[0].rstrip(';')
        obj = json.loads(constant)
        result = obj['classificacao']
        return result[self.id]
