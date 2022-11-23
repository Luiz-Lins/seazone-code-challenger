# Seazone Code Challenger
O objetivo desse repositório é a execução do Seazone code challenger.
O Desafio consiste na criação de três API's-Rest 

### Pré-requisitos

Antes de começar, é necessário que tenha instalado as seguintes ferramentas:
[Git](https://git-scm.com) & [Python](https://www.python.org/downloads/).  

Para prosseguir observe as seguintes instruções:


### 🎲 Rodando API-Rest (servidor)

```bash
# Clone este repositório

$ git clone <https://github.com/Luiz-Lins/seazone-code-challenger.git>

# Crie o ambiente virtual na raiz do projeto
$ python -m venv .venv

# Ative o ambiente virtual
$ .\.venv\Scripts\activate

# Instale as dependências
$ pip install -r requirements.txt

# Faça as migrações para o Banco de dados
$ python manage.py migrate

# Alimente o banco de dados para cada API com os seguintes comando:
  - API1 - Imovel
    $ python manage.py seed api1 --number=5

  - API2 - Anuncio
    $ python manage.py seed api2 --number=3

  - API3 - Reserva
    $ python manage.py seed api3 --number=8

# Crie um admin (Opcional)
$ python manage.py createsuperuser

# Execute a aplicação em modo de desenvolvimento
$ python manage.py runserver

# Por padrão do django o servidor inciará na porta:8000 - acesse <http://localhost:8000>
```
Acesse <http://localhost:8000>

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Django](https://www.djangoproject.com/start/overview/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [SQLite3](https://www.sqlite.org/index.html)
>