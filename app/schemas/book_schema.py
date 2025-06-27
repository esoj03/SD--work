from app.extensions import ma, db
from app.models.book_model import Book

class BookSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session

    isbn = ma.String(required=True)
    title = ma.String(required=True)
    author = ma.String(required=True)
    price = ma.Float(required=True)

book_schema = BookSchema()
books_schema = BookSchema(many=True)
