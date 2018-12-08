from flask_api import status
from lib.http.response import http_response
from lib.http.decorators import api_endpoint
from lib.crypto.cypher_manager import CypherManager as cy
from lib.token.token_manager import new_token, valid_token
from lib.helpers.date_operations import date_from_str, str_from_date


@api_endpoint()
def authenticate_view(request):
    username = request.data.get('username', None)
    password = request.data.get('password', None)
    if not username or not password:
        return http_response(
            { 'error': '"username" and "password" are required' },
            status.HTTP_400_BAD_REQUEST
        )
    
    user = { 'id': 1, 'name': 'sas' }
    # user = auth_user(username, password)
    # if not user:
    #     return http_response(
    #         { 'error': 'wrong username or password...' },
    #         status.HTTP_400_BAD_REQUEST
    #     )
    return http_response({ 'token': new_token(user) })

@api_endpoint()
def refresh_token_view(request):
    token = request.data.get('token', None)
    
    if not token:
        return http_response(
            {'error': '"token" is required'},
            status.HTTP_400_BAD_REQUEST
        )
    
    if not valid_token(token):
        return http_response(
            {'error': 'token invalid'},
            status.HTTP_400_BAD_REQUEST
        )
    
    decoded = cy.decode(token)
    response_data = { 
        'token': new_token({
            'id': decoded['user_id'],
            'name': decoded['username']
        })
    }
    return http_response(response_data) 
