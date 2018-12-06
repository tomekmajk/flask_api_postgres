from lib.crypto.cypher_manager import CypherManager as cy

def authenticate(request) -> dict:
    token_encoded = cy.encode({
        'user_id': 1,
        'username': 'sas',
        'expires': 'date_string_here(WIP)'
    })
    response = {
        'token': token_encoded.decode("utf-8")
    }
    return response

def decode_token(request) -> dict:
    ''' delete me l8r '''
    print(request.data)

    decoded = cy.decode(request.data['token'])
    return {
        'decoded': decoded if decoded else 'Invalid token!!!'
    }
