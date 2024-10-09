import json
import re

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    http_request = requests.get("https://ge.globo.com/futebol/brasileirao-serie-a/")
    soup = BeautifulSoup(http_request.content, "html.parser")
    resultado = soup.find('script', id='scriptReact')
    result = resultado.string
    constant = re.findall(r'const classificacao\s*=\s*(.*?);', result)
    obj = json.loads(constant[0])
    print(obj['classificacao'][0])