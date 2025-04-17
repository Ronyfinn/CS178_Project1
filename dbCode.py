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

def get_user_table():
    query = """
        SELECT 
            caffeine_log.id,
            caffeine_log.date,
            caffeine_log.time,
            caffeine_log.caffeine_mg,
            caffeine_log.serving_size,
            caffeine_log.effect,
            caffeine_log.taste,
            caffeine_log.context,
            caffeine_source.brand,
            caffeine_source.flavor,
            caffeine_source.cost_per_serving,
            caffeine_source.cost_per_100mg
        FROM caffeine_log
        JOIN caffeine_source ON caffeine_log.source_id = caffeine_source.id
        ORDER BY caffeine_log.date DESC, caffeine_log.time DESC
    """
    return execute_query(query)


