import psycopg2
from . import config

__all__ = ['create_tables', 'drop_tables']

def create_tables():
    """ create tables in postgresql database"""

    commands = (
            """
            CREATE TABLE IF NOT EXISTS site (
              site_id SERIAL PRIMARY KEY,
              site_name VARCHAR UNIQUE NOT NULL,
              site_location GEOGRAPHY(POINT, 4326)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sample_location (
              site_name VARCHAR UNIQUE NOT NULL,
              sample_location_id VARCHAR,
              sample_location GEOGRAPHY(POINT, 4326),
              PRIMARY KEY (site_name, sample_location_id)
            )
            """,
	    """
	    CREATE TABLE IF NOT EXISTS well_detail (
	      site_name VARCHAR,
	      well_id VARCHAR,
	      boring_id VARCHAR,
              PRIMARY KEY (site_name, well_id)
	    )
	    """,
	    """
	    CREATE TABLE IF NOT EXISTS boring_log (
	      site_name VARCHAR,
	      boring_id VARCHAR,
	      boring_location GEOGRAPHY(POINT, 4326)
	    )
	    """,
            """
            CREATE TABLE IF NOT EXISTS water_analysis (
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
            """,
            """
            CREATE TABLE IF NOT EXISTS waste_analysis (
              lab_id VARCHAR,
              site_name VARCHAR,
              program_id VARCHAR,
              sample_id VARCHAR,
              sample_date DATE,
              parameter VARCHAR,
              method VARCHAR,
              prep_method VARCHAR,
              analysis_result REAL,
              analysis_unit CHAR,
              analysis_flag CHAR(1),
              analysis_comment VARCHAR
            )
            """,
	    """
   	    CREATE TABLE IF NOT EXISTS water_limit (
	      site_name VARCHAR,
	      program_id VARCHAR,
	      sample_location_id VARCHAR,
	      parameter VARCHAR,
	      statistical_test VARCHAR,
	      background_start DATE,
	      background_end DATE,
	      lower_limit REAL NULL,
	      upper_limit REAL NOT NULL
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
	    DROP TABLE well_detail CASCADE
	    """,
            """
            DROP TABLE water_analysis CASCADE
            """,
            """
	    DROP TABLE waste_analysis CASCADE
            """,
	    """
	    DROP TABLE water_limit CASCADE
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
