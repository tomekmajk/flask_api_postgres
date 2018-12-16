import os
from psycopg2 import connect
from conf.app_config import APP_NAME, POSTGRES_CONFIG

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_schema_sql(shema_path: str):
    with open(shema_path) as schema_file:
        lines = schema_file.readlines()
        return  ''.join(lines)

def create_schema():
    conn = connect(**POSTGRES_CONFIG)
    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    cur.close()

    schema_sql = get_schema_sql(dir_path + '/db/sql_scripts/create_base_schema.sql').format(APP_NAME)
    cur = conn.cursor()
    print(schema_sql)
    cur.execute(schema_sql)
    cur.close()
    conn.commit()
    conn.close()
    print('FINISHED.')

if __name__ == '__main__':
    create_schema()
