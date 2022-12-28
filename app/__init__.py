from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
import os

SECRET_KEY = os.getenv('SECRET_KEY')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 370
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0


    with app.app_context():
        from .views.index import index_bp
        app.register_blueprint(index_bp)
    return app