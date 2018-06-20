import psycopg2
from enviropy.database import config


class Enviropy(object):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            try:
                print("connecting to database...")
                params = config.config(filename="database.ini", section="postgresql")
                _conxn = Enviropy._instance._conxn = psycopg2.connect(**params)

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                Enviropy._instance = None

            else:
                print("connection established")

        return cls._instance

    def __init__(self):
        self._conxn = self._instance._conxn

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conxn.close()

    def create_tables():
        """ create tables in database"""

        commands = (
            """
            CREATE TABLE IF NOT EXISTS site (
               site_name VARCHAR NOT NULL,
               site_location GEOGRAPHY(POINT, 4326),
			   PRIMARY KEY (site_name)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sample_location (
               site_name VARCHAR,
               sample_location_id VARCHAR,
               sample_location GEOGRAPHY(POINT, 4326),
               FOREIGN KEY (site_name) REFERENCES site(site_name)
            )
            """,
            """
			CREATE TABLE IF NOT EXISTS program (
			    program_id VARCHAR,
			    description VARCHAR,
			    PRIMARY KEY (program_id)
			)
			""",
            """
			CREATE TABLE IF NOT EXISTS global_params (
			    group_name VARCHAR,
			    param_name VARCHAR,
			    usgs_code VARCHAR(5),
                casrn VARCHAR,
                srsname VARCHAR NOT NULL,
                PRIMARY KEY (usgs_code)			   
			)
			""",
            """
	        CREATE TABLE IF NOT EXISTS well_detail (
	            site_name VARCHAR,
	            sample_location_id VARCHAR,
	            boring_id VARCHAR,
                FOREIGN KEY (site_name) REFERENCES site(site_name),
				FOREIGN KEY (sample_location_id) REFERENCES sample_location(sample_location_id)
	        )
	        """,
            """
	        CREATE TABLE IF NOT EXISTS boring_log (
	            site_name VARCHAR,
	            boring_id VARCHAR,
	            boring_location GEOGRAPHY(POINT, 4326),
				FOREIGN KEY (site_name) REFERENCES site(site_name)
	        )
	        """,
            """
            CREATE TABLE IF NOT EXISTS water_analysis (
                lab_id VARCHAR,
                site_name VARCHAR NOT NULL,
                program_id VARCHAR NOT NULL,
                sample_location_id VARCHAR NOT NULL,
                sample_date DATE,
                usgs_code VARCHAR(5) NOT NULL,
                analysis_result REAL,
                analysis_unit CHAR,
                analysis_pql REAL,
                analysis_mdl REAL,
                analysis_qualifier CHAR(1),
                analysis_method VARCHAR,
                analysis_comment VARCHAR,
			    FOREIGN KEY (site_name) REFERENCES site(site_name), 
			    FOREIGN KEY (program_id) REFERENCES program(program_id),
			    FOREIGN KEY (usgs_code) REFERENCES global_params(usgs_code)
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
                analysis_comment VARCHAR,
			    FOREIGN KEY (site_name) REFERENCES site(site_name), 
			    FOREIGN KEY (program_id) REFERENCES program(program_id),
			    FOREIGN KEY (usgs_code) REFERENCES global_params(usgs_code)
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
	            upper_limit REAL NOT NULL,
				FOREIGN KEY (site_name) REFERENCES site(site_name),
				FOREIGN KEY (program_id) REFERENCES program(program_id)
	        )
	        """,
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
	        """,
        )
