from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.revista_model import Revista
from app.schemas.revista_schema import revista_schema, revistas_schema

bp = Blueprint('revistas', __name__, url_prefix='/revistas')


# GET /revistas/ → listar todas
@bp.route("/", methods=["GET"])
def listar_revistas():
    revistas = Revista.query.all()
    return revistas_schema.jsonify(revistas), 200


# GET /revistas/<issn> → buscar por ISSN
@bp.route("/<string:issn>", methods=["GET"])
def buscar_revista(issn):
    revista = Revista.query.get(issn)
    if not revista:
        return jsonify({"erro": "Revista não encontrada"}), 404
    return revista_schema.jsonify(revista), 200


# POST /revistas/ → criar nova
@bp.route("/", methods=["POST"])
def criar_revista():
    dados = request.json
    errors = revista_schema.validate(dados)
    if errors:
        return jsonify(errors), 400

    if Revista.query.get(dados["issn"]):
        return jsonify({"erro": "ISSN já existente"}), 409

    nova_revista = revista_schema.load(dados)
    db.session.add(nova_revista)
    db.session.commit()
    return revista_schema.jsonify(nova_revista), 201


# PUT /revistas/<issn> → atualizar
@bp.route("/<string:issn>", methods=["PUT"])
def atualizar_revista(issn):
    revista = Revista.query.get(issn)
    if not revista:
        return jsonify({"erro": "Revista não encontrada"}), 404

    dados = request.json
    errors = revista_schema.validate(dados, partial=True)
    if errors:
        return jsonify(errors), 400

    revista.titulo = dados.get("titulo", revista.titulo)
    revista.area = dados.get("area", revista.area)
    revista.data_pub = dados.get("data_pub", revista.data_pub)
    revista.numero = dados.get("numero", revista.numero)
    revista.editora = dados.get("editora", revista.editora)
    revista.price = dados.get("price", revista.price)

    db.session.commit()
    return revista_schema.jsonify(revista), 200


# DELETE /revistas/<issn> → apagar
@bp.route("/<string:issn>", methods=["DELETE"])
def remover_revista(issn):
    revista = Revista.query.get(issn)
    if not revista:
        return jsonify({"erro": "Revista não encontrada"}), 404

    db.session.delete(revista)
    db.session.commit()
    return jsonify({"mensagem": "Revista removida com sucesso"}), 200
