import pymysql
import pymysql.cursors
import creds
import boto3

def get_conn():
    return pymysql.connect(
        host="projectone.cbiyiwuyi4a4.us-east-1.rds.amazonaws.com",
        user="admin",
        password="Mikfinne44!",
        db="ProjectOneCaffeineLog",
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

