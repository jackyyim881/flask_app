from flask import Blueprint

aws = Blueprint('aws', __name__)
from app.aws import routes
