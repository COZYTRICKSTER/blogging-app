from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_name=Config):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)

    from app.resources import resources_bp
    app.register_blueprint(resources_bp)

    return app
