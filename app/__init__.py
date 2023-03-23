from flask import Flask, request, redirect, url_for, flash, session
from config import Config
from .database.db import create_db
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '220f867f35c3854d9923ee22'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'hiking_app_cheerful'


create_db()
db = SQLAlchemy(app)
UPLOAD_FOLDER = 'static/uploads/'

mysql = MySQL(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'hiking_app_cheerful'

# mysql = MySQL()

from app.main import bp as main_bp
app.register_blueprint(main_bp)
from app.aws import aws as aws_bp
app.register_blueprint(aws_bp)   
from app.mysql import bp as aws_bp
app.register_blueprint(aws_bp) 
from app.errors import errors as errors_bp
app.register_blueprint(errors_bp)
from app.api import bp as api_bp
app.register_blueprint(api_bp)



# from app import models
# def create_app(config_class=Config):
#     db = SQLAlchemy() 
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'app.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.init_app(app)
#     app.config['MYSQL_HOST'] = '127.0.0.1'
#     app.config['MYSQL_USER'] = 'root'
#     app.config['MYSQL_PASSWORD'] = '12345678'
#     app.config['MYSQL_DB'] = 'hiking_app_cheerful'


#     # app.config['MYSQL_HOST'] = 'localhost'
#     # app.config['MYSQL_USER'] = 'root'
#     # app.config['MYSQL_PASSWORD'] = '12345678'
#     # app.config['MYSQL_PORT'] = 3306
#     # app.config['MYSQL_DB'] = 'hiking_app_cheerful'
#     # app.config['MYSQL_HOST'] = 'localhost'
#     # app.config['MYSQL_PORT'] = 3306
#     # app.config['MYSQL_USER'] = 'root'
#     # app.config['MYSQL_PASSWORD'] = '12345678'
#     # app.config['MYSQL_DB'] = 'hiking_app_cheerful'
#     # app.config['MYSQL_UNIX_SOCKET'] = None
#     # app.config['MYSQL_CONNECT_TIMEOUT'] = 10
#     # app.config['MYSQL_READ_DEFAULT_FILE'] = None
#     # app.config['MYSQL_CURSORCLASS'] = None
#     # app.config['MYSQL_USE_UNICODE'] = True
#     # app.config['MYSQL_CHARSET'] = 'utf8'
#     # app.config['MYSQL_SQL_MODE'] = None
#     # app.config['MYSQL_MULTIPLE_STATEMENTS'] = False
#     # app.config['MYSQL_FOUND_ROWS'] = False
#     # from mysql import mysql
#     # app.register_blueprint(mysql, url_prefix='/mysql')

    
#     app.config.from_object(config_class)

#     from app.main import bp as main_bp
#     app.register_blueprint(main_bp)
#     from app.aws import aws as aws_bp
#     app.register_blueprint(aws_bp)   
#     from app.mysql import bp as aws_bp
#     app.register_blueprint(aws_bp , url_prefix='/mysql') 
      
#     return app 
