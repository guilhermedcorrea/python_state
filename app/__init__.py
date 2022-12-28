from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from celery import Celery
from config import SQLALCHEMY_DATABASE_URI, UPLOADED_PHOTOS_DEST, SECRET_KEY


db = SQLAlchemy()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['UPLOADED_PHOTOS_DEST'] = UPLOADED_PHOTOS_DEST
    #app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = SECRET_KEY

    

    from .models.models import configure
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)


    #db.init_app(app)
    #configure(app)
    with app.app_context():
        #db.create_all()
        
      
        from .views.admin import Admin_bp
        app.register_blueprint(Admin_bp)

    return app
