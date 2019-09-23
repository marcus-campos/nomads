# Nomads Backend

Esta API tem como objetivo de prover os recursos para a aplicação de nômades digitais

Para criar a API, usamos:

* Ambiente: .venv
* Projeto: nomads

## Clonando o projeto

```bash
$ git clone https://github.com/marcus-campos/nomads
$ cd backend
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

## Testando a API

Agora podemos acessar nossa API, tanto na linha de comando, quanto usando ferramentas como curl...

```bash
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/places/
[
    {
        id: "3b183b29-2ed2-44d0-9102-8997516768a0",
        name: "WeWork",
        description: "A WeWork é uma empresa imobiliária americana que fornece espaços de trabalho compartilhados para startups de tecnologia e serviços para outras empresas.",
        address: "5ae501af-e5ec-4c9b-bcf9-54b721b0fb96"
    }
]
```