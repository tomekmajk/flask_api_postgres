from flask import request
from flask_api import FlaskAPI, status

from config import APP_ROOT
from lib.http.response import http_response
from lib.http.decorators import api_endpoint
from views.auth import authenticate_view, refresh_token_view


def url(route):
    return APP_ROOT + route

app = FlaskAPI(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route(url('/'))
def hello(): return http_response({'msg': 'Hi! :)'})

@app.route(url('/auth'), methods=['POST'])
def auth(): return authenticate_view(request)

@app.route(url('/refresh-token'), methods=['POST'])
def refresh_token(): return refresh_token_view(request)


if __name__ == "__main__":
    app.run(debug=True)
