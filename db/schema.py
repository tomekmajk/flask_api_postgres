from db_config import CONFIG
from psycopg2 import connect

def connect_to_db():
    conn = connect(**CONFIG)
    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)

    cur.close()
    conn.close()

if __name__ == '__main__':
    connect_to_db()
