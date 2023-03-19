from flask import render_template  , Flask

import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f"Container from {socket.gethostname()}!"



@app.route('/mainpage')
def index():    # put application's code here
    return render_template('index-original.html')


if __name__ == '__main__':
    app.run(debug=True)
