import psycopg2
from config import config

def connect():
    """ connect to postgresql database"""

    conn = None
    try:
        params = config()

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def create_tables():
    """ create tables in postgresql database"""

    commands = (
            """
            CREATE TABLE site (
              site_id SERIAL PRIMARY KEY,
              site_name VARCHAR(255) NOT NULL,
              site_location geography(POINT, 4326)
            )
            """,
            """
            CREATE TABLE sample_location (
              site_id ,
              sample_location_id ,
              sample_location geography(POINT, 4326)
            )
            """
            )
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)
        
        cur.close()

        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
