def test_top_livros_caros(client):
    res = client.get("/stats/books/top-expensive?limit=1")
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_livros_por_autor(client):
    res = client.get("/stats/books/author/Autor A")
    assert res.status_code == 200

def test_contar_livros(client):
    res = client.get("/stats/books/count")
    assert res.status_code == 200
    assert "total_livros" in res.json

def test_revistas_por_area(client):
    res = client.get("/stats/revistas/area/Educação")
    assert res.status_code == 200

def test_catalogo_por_preco(client):
    res = client.get("/stats/catalog/price/9.9")
    assert res.status_code == 200
    assert "livros" in res.json
    assert "revistas" in res.json
