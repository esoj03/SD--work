from flask import Flask
from .config import Config
from .extensions import db, migrate, ma

from app.routes.books import bp as books_bp
from app.routes.revistas import bp as revistas_bp
from app.routes.stats import bp as stats_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(books_bp)
    app.register_blueprint(revistas_bp)
    app.register_blueprint(stats_bp)

    @app.route("/")
    def index():
        return {"mensagem": "API do Projeto SD 2025 está online!"}

    return app
