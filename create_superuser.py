import os

from psycopg2 import connect
from lib.crypto.cypher_manager import encode
from conf.app_config import APP_NAME, POSTGRES_CONFIG

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_schema_sql(shema_path: str):
    with open(shema_path) as schema_file:
        lines = schema_file.readlines()
        return  ''.join(lines)

def create_superuser():
    email = input("Enter email: ")
    name = input("Enter name: ")
    psswd = input("Enter password: ")
    psswd_repeat = input("Repeat password: ")

    if psswd != psswd_repeat:
        raise Exception("Passwords do not match!")

    conn = connect(**POSTGRES_CONFIG)
    sql = get_schema_sql(
        dir_path + '/db/sql_scripts/create_superuser.sql'
    ).format(
        APP_NAME,
        email,
        name,
        encode({'password': psswd}).decode("utf-8")
    )
    cur = conn.cursor()
    print(sql)
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
    print('FINISHED.')

if __name__ == '__main__':
    create_superuser()
