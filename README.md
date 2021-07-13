# Escala de Atendimento Com Django

Projeto provê a melhoria na escala de médicos em postos de trabalho.
De forma que automatiza a escala via aplicação web com django.

## Link da aplicação
- Hospedado no Heroku: [clique aqui](https://escaladeatendimento.herokuapp.com/) 

## Para rodar a aplicação:
### 1° opção: clone a aplicação
`git clone https://github.com/MarcosAllysson/django_escala_de_atendimento`

Recomendado ter virtualenv instalado:
- Ative a venv: `source ./venv/bin/activate`

Instale as dependências:  
`pip install -r requirements.txt`

Suba aplicação:
`python manage.py runserver`

Abra a URL no browser:
`127.0.0.1:8000/`

### 2° opção: clone a aplicação e rode com docker-compose
`git clone https://github.com/MarcosAllysson/django_escala_de_atendimento`

Recomendado ter virtualenv instalado:
- Ative a venv: `source ./venv/bin/activate`

Build:  
`docker-compose build`

Suba aplicação:
`docker-compose up`

Abra a URL no browser:
`127.0.0.1:8000/`