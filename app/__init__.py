from flask import Flask, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from config import Config
from .database.db import create_db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '220f867f35c3854d9923ee22'

create_db()
db = SQLAlchemy(app)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.aws import aws as aws_bp
    app.register_blueprint(aws_bp)   
    return app 

from app import create_app
from app import models
# from app import models
