import os
from psycopg2 import connect
from db_config import CONFIG

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_schema_sql(shema_path: str):
    with open(shema_path) as schema_file:
        lines = schema_file.readlines()
        return  ''.join(lines)

def connect_to_db():
    conn = connect(**CONFIG)
    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    cur.close()

    schema_sql = get_schema_sql(dir_path + '/sql_scripts/create_schema.sql')
    cur = conn.cursor()
    print(schema_sql)
    cur.execute(schema_sql)
    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    connect_to_db()
