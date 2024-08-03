import os
import json
import psycopg2
from sqlalchemy import create_engine

def config(db_name):
    path = os.getcwd()
    with open(path + '/config.json') as f:
        data = json.load(f)[db_name]
    return data

def get_conn(conf, name_conn):
    try:
        conn = psycopg2.connect(
            host=conf['host'],
            database=conf['db'],
            user=conf['user'],
            password=conf['password'],
            port=conf['port']
        )
        print(f'[INFO] Connected to {name_conn} database')
        engine = create_engine(
            "postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}".format(
            user=conf['user'],
            password=conf['password'],
            host=conf['host'],
            port=conf['port'],
            db=conf['db']
            )
        )
        return conn, engine
    except Exception as e:
        print(f'[ERROR] Unable to connect to {name_conn} database')
        print(str(e))