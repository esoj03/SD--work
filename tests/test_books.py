from app.extensions import db
from app.models.book_model import Book

def test_criar_livro(client):
    res = client.post("/books/", json={
        "isbn": "001",
        "title": "Livro de Teste",
        "author": "Autor A",
        "price": 20.0
    })
    assert res.status_code == 201
    assert res.json["isbn"] == "001"

def test_listar_livros(client):
    res = client.get("/books/")
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_buscar_livro_existente(client):
    res = client.get("/books/001")
    assert res.status_code == 200
    assert res.json["isbn"] == "001"

def test_atualizar_livro(client):
    res = client.put("/books/001", json={"price": 25.0})
    assert res.status_code == 200
    assert res.json["price"] == 25.0

def test_remover_livro(client):
    res = client.delete("/books/001")
    assert res.status_code == 200
