# Projeto 4 - API REST de Filmes (Django REST Framework)

API REST para cadastro, consulta, edição e exclusão de **filmes** e **gêneros**, desenvolvida com Django e Django REST Framework. Conta com autenticação por token, filtros nas listagens e painel administrativo.

## Funcionalidades

- CRUD completo de filmes e gêneros (`ModelViewSet`)
- Autenticação por **Token** e por **Sessão**
- Leitura liberada para todos (`GET`); criação, edição e exclusão exigem login
- Filtros nas listagens com `django-filter`
- Interface navegável gerada pelo DRF
- Painel administrativo do Django com busca e filtros

## Tecnologias

- Python 3
- Django
- Django REST Framework
- django-filter

## Modelo de dados

**Generos**

| Campo | Descrição |
|-------|-----------|
| nome  | Nome do gênero |

**Filmes**

| Campo          | Descrição |
|----------------|-----------|
| titulo         | Título do filme |
| descricao      | Descrição / sinopse |
| ano_lancamento | Ano de lançamento |
| genero         | Chave estrangeira para `Generos` |
| duracao        | Duração (em minutos) |

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/phxdablio/project-4-evaluation-api-rest-framework.git
cd project-4-evaluation-api-rest-framework
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install django django-filter djangorestframework
```

### 4. Criar o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar um superusuário

```bash
python manage.py createsuperuser
```

### 6. Iniciar o servidor

```bash
python manage.py runserver
```

## Acessos

| Recurso | URL |
|---------|-----|
| Painel admin | http://localhost:8000/admin/ |
| API (interface DRF) | http://localhost:8000/api/ |
| Filmes | http://localhost:8000/api/filmes/ |
| Gêneros | http://localhost:8000/api/generos/ |
| Obter token | http://localhost:8000/api/token/ |

## Autenticação

O projeto usa `TokenAuthentication` e `SessionAuthentication`. A permissão padrão é `IsAuthenticatedOrReadOnly`:

- `GET`: livre
- `POST`, `PUT`, `PATCH`, `DELETE`: exigem autenticação

## Exemplos de uso (curl)

Os comandos abaixo usam a sintaxe do **CMD do Windows** (`curl.exe` e `^` para quebra de linha). No Linux/macOS, use `curl` e `\`.

**Listar filmes**

```bash
curl http://localhost:8000/api/filmes/
curl http://localhost:8000/api/filmes/3/
```

**Obter token de autenticação**

```bash
curl.exe -X POST http://127.0.0.1:8000/api/token/ ^
  -H "Content-Type: application/json" ^
  -d "{\"username\":\"seu_usuario\",\"password\":\"sua_senha\"}"
```

**Adicionar um filme**

```bash
curl.exe -X POST http://127.0.0.1:8000/api/filmes/ ^
  -H "Authorization: Token SEU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"titulo\":\"Interestelar\",\"descricao\":\"Uma exploração espacial.\",\"ano_lancamento\":2014,\"genero\":1,\"duracao\":169}"
```

**Editar e excluir** seguem o mesmo padrão, usando `PUT`/`PATCH` e `DELETE` em `/api/filmes/<id>/` com o header `Authorization`.

## Estrutura do projeto

```
projeto4/
├── filmes/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   └── views.py
├── projeto4/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## Licença

Projeto desenvolvido para fins educacionais.
