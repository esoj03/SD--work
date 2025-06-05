from app.extensions import db

class Book(db.Model):
    __tablename__ = 'books'

    isbn = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
