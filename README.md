# 📚 API REST de Livros e Revistas – Sistemas Distribuídos 2024/2025

## 📖 Sobre o Projeto

Esta é uma **API REST** desenvolvida para a disciplina de **Sistemas Distribuídos (2024/2025)**. Construída com **Python (Flask)** e **PostgreSQL**, a API permite o gerenciamento completo de **livros** e **revistas**, com suporte a **filtros avançados** e **estatísticas**.  
A arquitetura do projeto é modular e organizada, utilizando **Marshmallow** para validação, **SQLAlchemy** como ORM e **Pytest** para testes automatizados.

---

## ⚙️ Funcionalidades Principais

- CRUD completo para **livros** (`/books`)
- CRUD completo para **revistas** (`/revistas`)
- Filtros avançados e estatísticas (`/stats`)
- Testes automatizados com **Pytest**
- Gerenciamento de migrações de banco de dados com **Flask-Migrate**

---

## 🧰 Tecnologias Utilizadas

- Python 3.10+
- Flask
- SQLAlchemy
- Marshmallow + Marshmallow-SQLAlchemy
- PostgreSQL (via pgAdmin)
- Flask-Migrate
- Pytest + Pytest-Flask
- SQLite (para testes isolados)

---

## 🚀 Instalação e Execução

### ✅ Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL instalado e em execução
- pgAdmin (opcional, para interface gráfica do banco)
- Git

### 📦 Passo a Passo Completo

#### 1. Clonar o Repositório

```bash
git clone https://github.com/esoj03/SD--work
cd Trabalho_SD_25
````
#### 2. Criar Ambiente Virtual
```bash
python -m venv venv
````
#### 3. Ativar Ambiente Virtual
   
Linux/macOS:
```bash
source venv/bin/activate
````
Windows:
```bash
venv\Scripts\activate
````

#### 4. Instalar Dependências
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install --upgrade marshmallow-sqlalchemy
````

#### 5. Configurar Variáveis de Ambiente
Aviso: Nesta parte é necessario ter uma base de dados posgressql recomendamos instalar o postgresSQL juntamente com o PGadmin.
Primeiro deve-se criar a base de dados e depois no ficheiro .env substituir os campos utilizador, senha e nome da sua base de dados pelos respetivos valores corretos. 

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo (ou configure no terminal):
```bash
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://Utilizador:senha@localhost:5432/nome_da_sua_base_de_dados
````
🔒 Substitua utilizador e senha pelas suas credenciais PostgreSQL .

#### 6. Criar a Base de Dados
É recomendado criar a base de dados de forma manual no pgAdmim devido ao fato da arquitetura do projeto que utiliza o postgres como base de dados.
Utilize o terminal ou pgAdmin para criar a base de dados

#### 7. Inicializar Migrações
```bash
flask db init
````

#### 8. Criar Scripts de Migração
```bash
flask db migrate -m "init"
````

#### 9. Aplicar Migrações
```bash
flask db upgrade
````

#### 10. Executar a Aplicação
```bash
flask run
````

## 🧪 Executar Testes Automatizados
Rode os testes utilizando o Pytest:
````bash
pytest
````
🧪 O ambiente de testes usa SQLite, isolando o banco principal.
