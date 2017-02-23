import pyodbc
import pandas

__all__ = ['read_manages3']

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
	>>> cd = read_manages3('H:\INTERNAL\MANAGES_DATA\Cardinal\Cardinal\Site.mdb')

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
