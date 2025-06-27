from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.book_model import Book
from app.schemas.book_schema import book_schema, books_schema

bp = Blueprint('books', __name__, url_prefix='/books')


# GET /books/ → listar todos os livros
@bp.route("/", methods=["GET"])
def listar_livros():
    livros = Book.query.all()
    return books_schema.jsonify(livros), 200


# GET /books/<isbn> → buscar livro por ISBN
@bp.route("/<string:isbn>", methods=["GET"])
def buscar_livro(isbn):
    livro = Book.query.get(isbn)
    if not livro:
        return jsonify({"erro": "Livro não encontrado"}), 404
    return book_schema.jsonify(livro), 200


# POST /books/ → criar novo livro
@bp.route("/", methods=["POST"])
def criar_livro():
    dados = request.json
    errors = book_schema.validate(dados)
    if errors:
        return jsonify(errors), 400

    if Book.query.get(dados["isbn"]):
        return jsonify({"erro": "ISBN já existente"}), 409

    novo_livro = book_schema.load(dados)
    db.session.add(novo_livro)
    db.session.commit()
    return book_schema.jsonify(novo_livro), 201


# PUT /books/<isbn> → atualizar livro
@bp.route("/<string:isbn>", methods=["PUT"])
def atualizar_livro(isbn):
    livro = Book.query.get(isbn)
    if not livro:
        return jsonify({"erro": "Livro não encontrado"}), 404

    dados = request.json
    errors = book_schema.validate(dados, partial=True)
    if errors:
        return jsonify(errors), 400

    livro.title = dados.get("title", livro.title)
    livro.author = dados.get("author", livro.author)
    livro.price = dados.get("price", livro.price)

    db.session.commit()
    return book_schema.jsonify(livro), 200


# DELETE /books/<isbn> → remover livro
@bp.route("/<string:isbn>", methods=["DELETE"])
def remover_livro(isbn):
    livro = Book.query.get(isbn)
    if not livro:
        return jsonify({"erro": "Livro não encontrado"}), 404

    db.session.delete(livro)
    db.session.commit()
    return jsonify({"mensagem": "Livro removido com sucesso"}), 200
