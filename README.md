📚 API REST de Livros e Revistas – Sistemas Distribuídos 2024/2025

Este projeto consiste numa aplicação web construída com **Python (Flask)** e **PostgreSQL**, desenvolvida no âmbito da disciplina de **Sistemas Distribuídos**. A API permite o registo, consulta, atualização e remoção de livros e revistas, além de disponibilizar **estatísticas e filtros avançados**.

O projeto segue uma estrutura modular, usa **Marshmallow para validação**, **SQLAlchemy como ORM**, e tem uma **pasta de testes com Pytest**.

---

🧩 Funcionalidades Principais

- CRUD completo de livros (`/books`)
- CRUD completo de revistas (`/revistas`)
- Filtros avançados e estatísticas (`/stats`)
- Testes automatizados com Pytest
- Migração de base de dados com Flask-Migrate

---

⚙️ Tecnologias Utilizadas

- Python 3.10+
- Flask
- SQLAlchemy
- Marshmallow + Marshmallow-SQLAlchemy
- PostgreSQL (via pgAdmin)
- Flask-Migrate
- Pytest + Pytest-Flask
- SQLite (para testes isolados)

---

 🚀 Instalação e Execução
 1. Clonar o repositório
git clone https://github.com/esoj03/Trabalho_SD_25.git
cd Trabalho_SD_25

 2. Criar ambbiente virtual e instalar dependências
python -m venv venv
pip install -r requirements.txt

 3. Configurar variáveis de ambiente
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=postgresql://usuario:senha@localhost:5432/livraria_db

4. Criar a base de dados
createdb livraria_db

5. Criar as tabelas com Flask-Migrate
flask db init               # Apenas uma vez
flask db migrate -m "init" # Gera scripts
flask db upgrade            # Cria as tabelas no banco

▶️ Executar a Aplicação
flask run
http://127.0.0.1:5000
pytest
