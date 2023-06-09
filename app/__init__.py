from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    app.config['UPLOAD_FOLDER'] = 'static/uploads'

    from app.main.routes import main
    app.register_blueprint(main)

    return app