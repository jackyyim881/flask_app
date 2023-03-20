from flask import Blueprint
bp = Blueprint('mysql', __name__, url_prefix='/mysql')




from app.mysql import routes