import pymysql
import pymysql.cursors
import creds
import boto3

def get_conn():
    return pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_query(query, args =()):
    # Connect to the database
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(query, args)
            rows = cur.fetchall()
        return rows
    finally:
        conn.close()

def get_list_of_source():
    query = "SELECT brand, flavor FROM caffeine_source"
    return execute_query(query)

