import jwt
import os
from config import SECRET_KEY_ENV_VAR_NAME, SECRET_KEY


if SECRET_KEY:
    SECRET = SECRET_KEY
else:
    SECRET = os.environ.get(SECRET_KEY_ENV_VAR_NAME, None)
    if not SECRET:
        raise RuntimeError('ENV variable {} - not provided ...'.format(SECRET_KEY_ENV_VAR_NAME))

class CypherManager:
    
    @staticmethod
    def encode(data: dict) -> str:
        return jwt.encode(data, SECRET, algorithm='HS256')
    
    @staticmethod
    def decode(encoded: str) -> dict:
        try:
            return jwt.decode(encoded, SECRET, algorithms=['HS256'])
        except Exception as e:
            print(str(e))
            return None
