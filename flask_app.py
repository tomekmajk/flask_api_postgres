import threading
import time

from flask import request
from flask_api import FlaskAPI

from views.hello import hello_view

APP_BASE_URL_NAME = '/fun'

def url(route):
    return APP_BASE_URL_NAME + route

app = FlaskAPI(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route(url('/'))
def hello():
    return hello_view()

@app.route(url('/data'), methods=['GET', 'POST'])
def data():
    if len(request.data) == 0:
        r_data = None
    else:
        r_data= request.data
    return {'request data': r_data}


if __name__ == "__main__":
    app.run(debug=True)
