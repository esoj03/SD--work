from app.extensions import db

class Revista(db.Model):
    __tablename__ = 'revistas'

    issn = db.Column(db.String(9), primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    area = db.Column(db.String(100), nullable=False)
    data_pub = db.Column(db.Date, nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    editora = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
