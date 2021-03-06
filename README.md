[![Build Status](https://travis-ci.org/MarcoRLK/Requisitos04-DrogariaIdeal.svg?branch=master
)](https://travis-ci.org/MarcoRLK/Requisitos04-DrogariaIdeal)

# Drogaria Ideal

Este é um fork do repositório original destinado ao desenvolvimento do trabalho de Gerência de Configuração de Software.

## Alunos

|Nome|Matrícula|
|:--:|:-------:|
|Anderson Silva|14/0130004|
|Marco Kuroiva|16/0160464|

## Planejamento

Segue abaixo a lista de ferramentas das quais este projeto busca atender e seus status no atual projeto:

|           |Environment|Continous Integration|Configuration|Build|Packing|
|:---------:|:---------:|:-------------------:|:-----------:|:---:|:-----:|
|Ferramenta:|Docker|Travis|Chef|Gulp|Egg|
|Status:    |Dois services: web e db|Passou build com testes e o flake8 está comentado|X|Rodando através do django-gulp|Basta rodar o comando indicado no tutorial abaixo|

## Links relevantes:

- Travis:

  https://travis-ci.org/MarcoRLK/Requisitos04-DrogariaIdeal/

- Documentação do django-gulp:

  https://pypi.python.org/pypi/django-gulp


## Como rodar:

Pré-requisitos:
- Git
- Docker + Docker-Compose

### Faça um clone do repositório:

`git clone https://github.com/MarcoRLK/Requisitos04-DrogariaIdeal.git`

### Entre na pasta do projeto, onde se encontram os arquivos do docker:

`cd Requisitos04-DrogariaIdeal/Drogaria Ideal`

### Inicie um container construindo a imagem:

`sudo docker-compose up --build`

**Pode levar alguns minutos**

### Acesse a aplicação:

Abra o navegador e acesse:

`http://localhost:8000/`

### Para rodar os testes:

`sudo docker-compose run web py.test`

### Para rodar o flake8:

`sudo docker-compose run web flake8`

### Para gerar o egg do projeto (empacotar):

`sudo docker-compose run  python setup.py bdist_egg`
O egg se encontrará na pasta:
**Requisitos04-DrogariaIdeal/dist**

### E o Gulp?

Ao levantar o container, você já estará executando o gulp. Isso graças ao django-gulp, que sobrescreve o './manage.py' e o './manage.py collectstatic' para que eles executem o comando 'gulp'.
Para verificar os resultados da sua execução, bastar observar o terminal e a pasta:
**Requisitos04-DrogariaIdeal/static/gulp/**
