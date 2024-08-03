import connection
import os
import sqlparse
import pandas as pd

if __name__ == '__main__':
    #production db
    marketplace_conf= connection.config('marketplace_prod')
    conn, engine = connection.get_conn(marketplace_conf, 'DataSource')
    cursor_marketplace = conn.cursor()
    
    #dwh db
    dwh_conf = connection.config('dwh')
    conn_dwh, engine_dwh = connection.get_conn(dwh_conf, 'DWH')
    cursor_dwh = conn_dwh.cursor()
    
    #query
    query_path = os.getcwd() + '/query/'
    
    query = sqlparse.format(
        open(query_path + 'query.sql', 'r').read(), strip_comments=True,
    ).strip()
    
    dwh_design = sqlparse.format(
        open(query_path + 'dwh_design.sql', 'r').read(), strip_comments=True,
    ).strip()
    
    try:
        # get data from marketplace/prod db
        print(f'[INFO] Service ETL process started')
        df = pd.read_sql(query, engine)
        print(df)
        
        # create table in dwh db
        cursor_dwh.execute(dwh_design)
        conn_dwh.commit()
        
        # ingest data to dwh db
        df.to_sql(
            'dim_orders_hilmi',
            engine_dwh,
            schema='public',
            if_exists='replace',
            index=False
        )
        
    except Exception as e:
        print(f'[ERROR] Unable to complete ETL process')
        print(str(e))