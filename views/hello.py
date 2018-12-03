from flask import jsonify

def hello_view():
    msg = {'msg': 'Helloł!'}
    return msg
