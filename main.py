import psycopg2
import queries
from executors import health
from executors import education
from executors import culture

from config import config

""" Connect to the PostgreSQL database server """
conn = None
try:
    # read connection parameters
    params = config()

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)

    # create a cursor
    cur = conn.cursor()
    
    # create table if table doesn't exist
    cur.execute(queries.create_table_sql)
    
    # insert data into table
    health.save_posts(cur)
    education.save_posts(cur)
    culture.save_posts(cur)

# close the communication with the PostgreSQL
    cur.close()
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
