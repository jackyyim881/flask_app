from flask import render_template
from app import app

from app.errors import errors


@errors.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@errors.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500
