import pymysql
import pymysql.cursors
#import creds
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

def get_list_of_source():
    query = """
        SELECT 
            log.id AS log_id,
            log.date,
            log.time,
            log.caffeine_mg,
            log.serving_size,
            log.effect,
            log.taste,
            log.context,
            source.brand,
            source.flavor,
            source.cost_per_serving,
            source.cost_per_100mg
        FROM caffeine_log AS log
        JOIN caffeine_source AS source ON log.source_id = source.id
        ORDER BY log.date DESC, log.time DESC
    """
    return execute_query(query)


