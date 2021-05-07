import psycopg2
from config import config

# using fetchone
def get_vendors():
    sql = 'SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name;'
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        print(f'The number of parts: {cur.rowcount}')
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() 

# using fetchall
def get_parts():
    sql = 'SELECT * FROM vendors ORDER BY vendor_id;'
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        print('The number of parts:', cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# using fetchmany
def iter_rows(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_vendor_parts():
    conn = None
    sql = """
        SELECT part_name, vendor_name
        FROM parts
        INNER JOIN vendor_parts ON vendor_parts.part_id = parts.part_id
        INNER JOIN vendors ON vendors.vendor_id = vendor_parts.vendor_id
        ORDER BY part_name;"""
    try:
        conn = psycopg2.connect(**config())
        cur = conn.cursor()
        cur.execute(sql)
        for row in iter_rows(cur, 10):
            print(row)
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    

# get_vendors()
# get_parts()
get_vendor_parts()
