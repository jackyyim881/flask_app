from flask import Blueprint

aws = Blueprint('aws', __name__, url_prefix='/aws')
from app.aws import routes
