from datetime import datetime, timedelta
from lib.crypto.cypher_manager import CypherManager as cy
from lib.helpers.date_operations import str_from_date, date_from_str

try:
    from config import JWT_LIFETIME_MINUTES
    JWT_LIFETIME = JWT_LIFETIME_MINUTES
except:
    JWT_LIFETIME = 9999


def valid_token(token: str) -> bool:
    decoded = cy.decode(token)
    if not decoded: return False
    expires = decoded.get('expires', None)
    if not expires: return False
    return date_from_str(expires) > datetime.now()

def new_token(user: dict) -> str:
    token_data = {
        'user_id': user['id'],
        'username': user['name'],
        'expires': str_from_date(datetime.now() + timedelta(minutes=JWT_LIFETIME))
    }
    token_encoded = cy.encode(token_data)
    return token_encoded.decode("utf-8")
