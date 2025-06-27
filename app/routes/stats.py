from flask import Blueprint, request, jsonify
from sqlalchemy import desc, asc, extract
from app.extensions import db
from app.models.book_model import Book
from app.models.revista_model import Revista
from app.schemas.book_schema import books_schema
from app.schemas.revista_schema import revistas_schema

bp = Blueprint('stats', __name__, url_prefix='/stats')

# --- BOOKS ---

# GET /stats/books/top-expensive?limit=N
@bp.route('/books/top-expensive')
def top_livros_caros():
    limit = int(request.args.get('limit', 10))
    livros = Book.query.order_by(desc(Book.price)).limit(limit).all()
    return books_schema.jsonify(livros)

# GET /stats/books/top-cheap?limit=N
@bp.route('/books/top-cheap')
def top_livros_baratos():
    limit = int(request.args.get('limit', 10))
    livros = Book.query.order_by(asc(Book.price)).limit(limit).all()
    return books_schema.jsonify(livros)

# GET /stats/books/count
@bp.route('/books/count')
def contar_livros():
    total = Book.query.count()
    return jsonify({"total_livros": total})

# GET /stats/books/author/<autor>
@bp.route('/books/author/<string:autor>')
def livros_por_autor(autor):
    livros = Book.query.filter(Book.author.ilike(f'%{autor}%')).all()
    return books_schema.jsonify(livros)

# DELETE /stats/books/author/<autor>
@bp.route('/books/author/<string:autor>', methods=["DELETE"])
def remover_livros_por_autor(autor):
    livros = Book.query.filter(Book.author.ilike(f'%{autor}%')).all()
    count = len(livros)
    if count == 0:
        return jsonify({"mensagem": "Nenhum livro encontrado para o autor."}), 404
    for livro in livros:
        db.session.delete(livro)
    db.session.commit()
    return jsonify({"mensagem": f"{count} livro(s) removido(s) do autor {autor}."})


# --- REVISTAS ---

# GET /stats/revistas/area/<area>
@bp.route('/revistas/area/<string:area>')
def revistas_por_area(area):
    revistas = Revista.query.filter(Revista.area.ilike(f'%{area}%')).all()
    return revistas_schema.jsonify(revistas)

# GET /stats/revistas/editora/<nome>
@bp.route('/revistas/editora/<string:nome>')
def revistas_por_editora(nome):
    revistas = Revista.query.filter(Revista.editora.ilike(f'%{nome}%')).all()
    return revistas_schema.jsonify(revistas)

# GET /stats/revistas/ano/<int:ano>
@bp.route('/revistas/ano/<int:ano>')
def revistas_por_ano(ano):
    revistas = Revista.query.filter(extract('year', Revista.data_pub) == ano).all()
    return revistas_schema.jsonify(revistas)

# GET /stats/revistas/mais-cara
@bp.route('/revistas/mais-cara')
def revista_mais_cara():
    revista = Revista.query.order_by(desc(Revista.price)).first()
    if revista:
        return revistas_schema.jsonify([revista])
    return jsonify({"mensagem": "Nenhuma revista encontrada."}), 404

# GET /stats/revistas/count
@bp.route('/revistas/count')
def contar_revistas():
    total = Revista.query.count()
    return jsonify({"total_revistas": total})


# --- CATÁLOGO ---

# GET /stats/catalog/price/<valor>
@bp.route('/catalog/price/<float:valor>')
def catalogo_por_preco(valor):
    livros = Book.query.filter(Book.price == valor).all()
    revistas = Revista.query.filter(Revista.price == valor).all()
    return jsonify({
        "livros": books_schema.dump(livros),
        "revistas": revistas_schema.dump(revistas)
    })
