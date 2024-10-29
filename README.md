# Topico Especial

## Trabalho para aula topico especial (Python)

### Como rodar

Tenha o [python](https://www.python.org/downloads/) instalado na sua máquina (versão recomendada 3.12)

```
$ pip install --no-cache-dir -r requirements.txt # Instale as dependencias do projeto
$ python app/__init__.py                         # Execute a api
```

### Como rodar com Docker

Tenha o [docker](https://www.docker.com/get-started/) instalado na sua máquina

```
$ docker pull python:3.12-slim
$ docker build -t leoraisilva/topico_especial .
$ docker run -p 5000:5000 leoraisilva/topico_especial
```

## API em Python que permite ver a tabela atualizada das principais ligas de futebol mundial

A API permite obter a tabela da tabela da liga ou filtrar um time por sua posição na tabela 

## Ligas suportadas

Brasileirao

_Primeira divisão do campeonato brasileiro_

Você pode acessar os recursos da Série A do *Brasileirao* nas rotas

```
http://{host}/api/v1/brasileirao/
http://{host}/api/v1/brasileirao/<posicao>
```

** Brasileirao B **

_Segunda divisão do campeonato brasileiro_

Você pode acessar os recursos da Série B do *Brasileirao* nas rotas

```
http://{host}/api/v1/brasileirao-serie-b/
http://{host}/api/v1/brasileirao-serie-b/<posicao>
```

** Premier League **

_Primeira divisão do campeonato inglês_

Você pode acessar os recursos da *Premier League* nas rotas

```
http://{host}/api/v1/premier-league/
http://{host}/api/v1/premier-league/<posicao>
```

** La Liga **

_Primeira divisão do campeonato espanhol_

Você pode acessar os recursos da *La Liga* nas rotas

```
http://{host}/api/v1/la-liga/
http://{host}/api/v1/la-liga/<posicao>
```

** Bundesliga **

_Primeira divisão do campeonato alemão_

Você pode acessar os recursos da *Bundesliga* nas rotas

```
http://{host}/api/v1/bundesliga/
http://{host}/api/v1/bundesliga/<posicao>
```

** League 1 **

_Primeira divisão do campeonato francês_

Você pode acessar os recursos da *League 1* nas rotas

```
http://{host}/api/v1/league-one/
http://{host}/api/v1/league-one/<posicao>
```

** Série A **

_Primeira divisão do campeonato italiano_

Você pode acessar os recursos da *Série A* nas rotas

```
http://{host}/api/v1/serie-a/
http://{host}/api/v1/serie-a/<posicao>
```

** Saudita **

_Primeira divisão do campeonato saudita_

Você pode acessar os recursos do *Campeonato Saudita* nas rotas

```
http://{host}/api/v1/saudita/
http://{host}/api/v1/saudita/<posicao>
```
