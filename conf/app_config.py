APP_NAME = 'flap'
API_ROOT = '/{}/api'.format(APP_NAME)
SECRET_KEY = 'ultra_secretLOL'
SECRET_KEY_ENV_VAR_NAME = 'TOP_SECRET_APP_KEY'
# JWT_LIFETIME_MINUTES = 30
POSTGRES_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'flask_app',
    'user': 'postgres',
    'password': 'postgres'
}
