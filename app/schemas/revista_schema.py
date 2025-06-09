from app.extensions import ma, db
from app.models.revista_model import Revista

class RevistaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Revista
        load_instance = True
        sqla_session = db.session

    issn = ma.String(required=True)
    titulo = ma.String(required=True)
    area = ma.String(required=True)
    data_pub = ma.Date(required=True)
    numero = ma.Integer(required=True)
    editora = ma.String(required=True)
    price = ma.Float(required=True)

revista_schema = RevistaSchema()
revistas_schema = RevistaSchema(many=True)
