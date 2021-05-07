import psycopg2
from config import config
    
def connect():
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print('PostgreSQL database version:')   
        cur.execute('Select version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

connect()


#         Simple way

# conn = psycopg2.connect(
#     host="localhost",
#     database="postgres",
#     user="pp2user",
#     password="Perfect777"
# )
#     or 
# info = {'host': 'localhost', 'database': 'postgres', 'user': 'pp2user', 'password': 'Perfect777'}
# conn = psycopg2.connect(**info)
# 
# print('Connecting to the PostgreSQL database...')
# cur = conn.cursor()
# print('PostgreSQL database version:')  
# cur.execute('Select version()')
# db_version = cur.fetchone()
# print(db_version)
# cur.close()

# if conn is not None:
#     conn.close()
#     print('Database connection closed.')