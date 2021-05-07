import psycopg2
from config import config

def delete_vendor(part_id):
    conn = None
    sql = 'DELETE FROM parts WHERE part_id = %s'
    rows_deleted = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (part_id,))
        rows_deleted = cur.rowcount
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return rows_deleted

part_id = int(input())
print(f'Number of deleted rows: {delete_vendor(part_id)}')