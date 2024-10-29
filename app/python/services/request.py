import json
import re

import requests
from bs4 import BeautifulSoup

class Tabela:
    def brasileiro_a():
        raw = requests.get("https://ge.globo.com/futebol/brasileirao-serie-a/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0])['classificacao']
        return table


    def posicao_brasileiro_a(pos):
        if pos < 0 or pos > 19:
            return '{"error": "skdki"}'
    
        raw = requests.get("https://ge.globo.com/futebol/brasileirao-serie-a/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0])['classificacao']
        return table[pos]


    def brasileiro_b():
        raw = requests.get("https://ge.globo.com/futebol/brasileirao-serie-b/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0])['classificacao']
        return table
    

    def posicao_brasileiro_b(pos):
        if pos < 0 or pos > 19:
            return '{"error": "skdki"}'
    
        raw = requests.get("https://ge.globo.com/futebol/brasileirao-serie-b/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0])['classificacao']
        return table[pos]


    def ingles(): 
        raw = requests.get("https://ge.globo.com/futebol/brasileirao-serie-b/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table


    def posicao_ingles(pos):
        if pos < 0 or pos > 19:
            return '{"error": "skdki"}'
    
        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-ingles/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table[pos]


    def alemao():
        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-alemao/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table


    def posicao_alemao(pos):
        if pos < 0 or pos > 17:
            return '{"error": "skdki"}'
    
        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-alemao/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table[pos]
    

    def espanhol():
        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-espanhol/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table


    def posicao_espanhol(pos):
        if pos < 0 or pos > 19:
            return '{"error": "skdki"}'
    
        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-espanhol/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table[pos]
    

    def italiano():
        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-italiano/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table


    def posicao_italiano(pos):
        if pos < 0 or pos > 19:
            return '{"error": "skdki"}'
    
        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-italiano/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table[pos]
    

    def frances():
        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-frances/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table


    def posicao_frances(pos):
        if pos < 0 or pos > 17:
            return '{"error": "skdki"}'
    
        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-frances/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table[pos]
    

    def saudita():
        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-saudita/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table
    

    def posicao_saudita(pos):
        if pos < 0 or pos > 17:
            return '{"error": "skdki"}'

        raw = requests.get("https://ge.globo.com/futebol/futebol-internacional/futebol-saudita/")
        html = BeautifulSoup(raw.content, "html.parser")
        content = html.find('script', id='scriptReact').string
        data = re.findall(r'const classificacao\s*=\s*(.*?);', content)
        table = json.loads(data[0].rstrip(';'))['classificacao']
        return table[pos]

