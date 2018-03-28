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
              site_name VARCHAR NOT NULL,
              site_location GEOGRAPHY(POINT, 4326)
            )
            """,
            """
            CREATE TABLE sample_location (
              site_name VARCHAR NOT NULL,
              sample_location_id VARCHAR,
              sample_location GEOGRAPHY(POINT, 4326)
            )
            """,
            """
            CREATE TABLE water_analysis (
              lab_id VARCHAR,
              site_name VARCHAR,
              program_id VARCHAR,
              sample_location_id VARCHAR,
              sample_date DATE,
              parameter VARCHAR,
              filtered BOOL,
              analysis_result REAL,
              analysis_unit CHAR,
              analysis_pql REAL,
              analysis_mdl REAL,
              analysis_qualifier CHAR(1),
              analysis_matrix VARCHAR,
              analysis_method VARCHAR,
              analysis_comment VARCHAR
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

def drop_tables():
    """ drop tables"""

    commands = (
            """
            DROP TABLE site CASCADE
            """,
            """
            DROP TABLE sample_location CASCADE
            """,
            """
            DROP TABLE water_analysis CASCADE
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
