import pyodbc
import pandas
from configparser import ConfigParser

__all__ = ['read_manages3']

def config(filename='database.ini', section='manages'):
    """configure manages database"""
    
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def read_manages3(mdb_path):
    """
	Function to read a MANAGES 3.x database and return
	the data in a pandas DataFrame for analysis.

	Parameters
	----------
	mdb_path : str
	    The path to the MANAGES 3.x Site.mdb file.

    Returns
    -------
    DataFrame :  pandas DataFrame
        returns a pandas DataFrame.

	Examples
	--------
	>>> from enviropy.external import read_manages3
	>>> data = read_manages3('H:\INTERNAL\MANAGES_DATA\Cardinal\Cardinal\Site.mdb')

	"""

    driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
    database = mdb_path

    conxn = pyodbc.connect('DRIVER={0};DBQ={1}'.format(driver, database))

    query = """

    SELECT sample_results.lab_id, sample_results.location_id,
	sample_results.sample_date, site_parameters.param_name,
	sample_results.lt_measure, sample_results.analysis_result,
	site_parameters.default_unit
	FROM sample_results LEFT JOIN site_parameters
	ON sample_results.storet_code = site_parameters.storet_code

    """

    data = pandas.read_sql(query, conxn)

    conxn.close()

    return data


class Manages():
    """
    Function to read a MANAGES 4.x database and return
    the data in a pandas DataFrame for analysis.

    Parameters
    ----------
    server : str
        The name of the server.
		
    database : str
	The name of the database

    Returns
    -------
    DataFrame :  pandas DataFrame
        returns a pandas DataFrame.

    Examples
    --------
    >>> from enviropy.external import manages
    >>> db = manages.Manages(server=server_name, database=database_name)

    """
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
			
        try:
            params = config()
            conn = pyodbc.connect(**params)
	        
        except (Exception, pyodbc.DatabaseError) as error:
            print(error)
		
        return cls._instance
				
    def __init__(self):
        self.connection = self._instance.connection

    def __enter__(self):
        return self
    
    def __exit__(Self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def site_names(self):
        return pandas.read_sql("SELECT NAME FROM SITE", self.connection)
     
    def get_results(self):
        
        query = """

        SELECT site.site_id, site.name,
	sample_results.lab_id, sample_results.location_id,
	sample_results.sample_date, site_parameters.param_name,
	sample_results.lt_measure, sample_results.analysis_result,
	sample_results.detection_limit, sample_results.RL,
	sample_results.flags, site_parameters.default_unit
	
	FROM sample_results 
	    LEFT JOIN site_parameters
	        ON sample_results.storet_code = site_parameters.storet_code AND sample_results.site_id = site_parameters.site_id	
            LEFT JOIN locations
		ON locations.site_id = sample_results.site_id AND locations.location_id = sample_results.location_id
	    LEFT JOIN site
                ON site.site_id = locations.site_id	
        """

        return pandas.read_sql(query, self.connection)
