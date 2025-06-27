def test_criar_revista(client):
    res = client.post("/revistas/", json={
        "issn": "1234-5678",
        "titulo": "Revista Teste",
        "area": "Educação",
        "data_pub": "2024-01-01",
        "numero": 1,
        "editora": "Editora X",
        "price": 9.9
    })
    assert res.status_code == 201
    assert res.json["issn"] == "1234-5678"

def test_listar_revistas(client):
    res = client.get("/revistas/")
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_buscar_revista(client):
    res = client.get("/revistas/1234-5678")
    assert res.status_code == 200
    assert res.json["titulo"] == "Revista Teste"
