import json
import re

import requests
from bs4 import BeautifulSoup


class Football:
    def tabela(self, url):
        raw = requests.get(url)
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0])['classificacao']
        return table

    def tabela_internacional(self, url):
        raw = requests.get(url)
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?)\n', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table

    def jogos(self, url):
        raw = requests.get(url)
        html_parser = BeautifulSoup(raw.content, "html.parser")
        content = html_parser.find('script', id='scriptReact').string
        data = re.findall(r'const listaJogos\s*=\s*(.*?)\n', content)
        list = data[0][1:-1]
        local = '{"da'
        lists = list.split(local)
        test = []
        for i in range(1, len(lists)):
            test.append(json.loads(local + lists[i][0:-1]))
        return test

    def brasileiro_a(self):
        return self.tabela_internacional("https://ge.globo.com/futebol/brasileirao-serie-a/")

    def posicao_brasileiro_a(self, pos):
        if pos < 0 or pos > 19:
            return '{"error": "skdki"}'
        table = self.tabela("https://ge.globo.com/futebol/brasileirao-serie-a/")
        return table[pos]

    def brasileiro_b(self):
        return self.tabela_internacional("https://ge.globo.com/futebol/brasileirao-serie-b/")

    def posicao_brasileiro_b(self, pos):
        if pos < 0 or pos > 19:
            return '{"error": "skdki"}'
        table = self.tabela("https://ge.globo.com/futebol/brasileirao-serie-b/")
        return table[pos]

    def ingles(self):
        return self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-ingles/")

    def posicao_ingles(self, pos):
        if pos < 0 or pos > 19:
            return '{"error": "skdki"}'
        table = self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-ingles/")
        return table[pos]

    def alemao(self):
        return self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-alemao/")

    def posicao_alemao(self, pos):
        if pos < 0 or pos > 17:
            return '{"error": "skdki"}'
        table = self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-alemao/")
        return table[pos]

    def espanhol(self):
        return self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-espanhol/")

    def posicao_espanhol(self, pos):
        if pos < 0 or pos > 19:
            return '{"error": "skdki"}'
        table = self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-espanhol/")
        return table[pos]

    def italiano(self):
        return self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-italiano/")

    def posicao_italiano(self, pos):
        if pos < 0 or pos > 19:
            return '{"error": "skdki"}'
        table = self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-italiano/")
        return table[pos]

    def frances(self):
        return self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-frances/")

    def posicao_frances(self, pos):
        if pos < 0 or pos > 17:
            return '{"error": "skdki"}'
        table = self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-frances/")
        return table[pos]

    def saudita(self):
        return self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-saudita/")

    def posicao_saudita(self, pos):
        if pos < 0 or pos > 17:
            return '{"error": "skdki"}'
        table = self.tabela_internacional("https://ge.globo.com/futebol/futebol-internacional/futebol-saudita/")
        return table[pos]

    #jogos
    def games_brasileirao(self):
        return self.jogos("https://ge.globo.com/futebol/brasileirao-serie-a/")

    def games_brasileiraoB(self):
        return self.jogos("https://ge.globo.com/futebol/brasileirao-serie-b/")

    def games_ingles(self):
        return self.jogos("https://ge.globo.com/futebol/futebol-internacional/futebol-ingles/")

    def games_espanhol(self):
        return self.jogos("https://ge.globo.com/futebol/futebol-internacional/futebol-espanhol/")

    def games_italiano(self):
        return self.jogos("https://ge.globo.com/futebol/futebol-internacional/futebol-italiano/")

    def games_frances(self):
        return self.jogos("https://ge.globo.com/futebol/futebol-internacional/futebol-frances/")

    def games_alemao(self):
        return self.jogos("https://ge.globo.com/futebol/futebol-internacional/futebol-alemao/")

    def games_saudita(self):
        return self.jogos("https://ge.globo.com/futebol/futebol-internacional/futebol-saudita/")
