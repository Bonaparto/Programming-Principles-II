import psycopg2

conn_info = {'host': 'localhost', 'database': 'test', 'user': 'pp2user', 'password': 'Perfect777'}
conn = psycopg2.connect(**conn_info)
cur = conn.cursor()
command = "DROP TABLE defense"
cur.execute(command)
#           Connecting
# cur.execute('Select version();')
# print(f'PostgreSQL version: {cur.fetchone()}')

#       Creating table
# command = """
#         CREATE TABLE defense (
#             ID SERIAL PRIMARY KEY,
#             Letters VARCHAR(255) NOT NULL,
#             Integers VARCHAR(255) NOT NULL
#         )
#         """

#        Inserting into table
# command = "INSERT INTO defense(letters, integers) VALUES(%s, %s);"
# cur.execute(command, ('abc', 'wtf'))

#        Updating data
# command = """UPDATE defense 
#         SET Letters = %s
#         WHERE INTEGERS = %s
#           """
# cur.execute(command, ('xyz', 'wtf'))


#         Querying data
# command = "SELECT Letters, Integers FROM defense"
# cur.execute(command)
# print(cur.fetchone())

#         Deleting data
# command = "DELETE FROM defense WHERE Letters = %s"
# cur.execute(command, (input(),))

conn.commit()
cur.close()
conn.close()