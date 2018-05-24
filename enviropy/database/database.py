import psycopg2
from . import config

__all__ = ['create_tables', 'drop_tables']

class Enviropy(object):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            try:
                params = config.config(filename='database.ini', section='postgres')
                _conxn = Enviropy._instance._conxn = psycopg2.connect(**params)

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                Enviropy._instance = None

        return cls._instance

    def __init__(self):
        self._conxn = self._instance._conxn

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conxn.close()
  
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
