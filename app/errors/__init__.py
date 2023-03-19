from flask import Blueprint

bp = Blueprint('handlers', __name__)

from app.errors import handlers
