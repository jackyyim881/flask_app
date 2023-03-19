from flask import render_template, flash, redirect, url_for, request, g, session
from app.main import bp

import socket

@bp.route('/')
def hello_world():
    return f"Container from {socket.gethostname()}!"

@bp.route('/mainpage')
def index():    # put application's code here
    # return render_template('index-original.html')
    return render_template('index-original.html')
