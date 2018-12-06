import threading
import time

from flask import request
from flask_api import FlaskAPI

from views.hello import hello_view
from views.auth import authenticate, decode_token
from config import APP_ROOT

def url(route):
    return APP_ROOT + route

app = FlaskAPI(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route(url('/'))
def hello():
    return hello_view()

@app.route(url('/auth'), methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        return authenticate(request)
    return {
        'msg': 'give me username and password!'
    }

@app.route(url('/decode'), methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        return decode_token(request)
    else:
        return {
            'msg': 'give me token!'
        }


if __name__ == "__main__":
    app.run(debug=True)
