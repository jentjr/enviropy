import pyodbc
import pandas

__all__ = ['read_manages3', 'read_manages4']

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

def read_manages4(server, database):
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
	>>> from enviropy.external import read_manages4
	>>> data = read_manages4(server=server_name, database=database_name)

	"""

    driver = '{SQL Server Native Client 11.0}'

    conxn = pyodbc.connect('DRIVER={0};SERVER={1};DATABASE={2};TRUSTED_CONNECTION=Yes'.format(driver, server, database))

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

    data = pandas.read_sql(query, conxn)

    conxn.close()

    return data