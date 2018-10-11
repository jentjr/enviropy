import pyodbc
import pandas
from enviropy.database import config

__all__ = ["read_manages3"]


def _list_or_tuple(x):
    return isinstance(x, (list, tuple))


def _flatten(sequence, to_expand=_list_or_tuple):
    for item in sequence:
        if to_expand(item):
            for subitem in _flatten(item, to_expand):
                yield subitem
        else:
            yield item


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

    driver = "{Microsoft Access Driver (*.mdb, *.accdb)}"
    database = mdb_path

    conxn = pyodbc.connect("DRIVER={0};DBQ={1}".format(driver, database))

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


class Manages(object):
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
    >>> db = manages.Manages()

    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            try:
                print("connecting to manages database...")
                params = config.config(filename="database.ini", section="manages")
                _conxn = Manages._instance._conxn = pyodbc.connect(**params)

            except (Exception, pyodbc.DatabaseError) as error:
                print(error)
                Manages._instance = None

            else:
                print("connection established")

        return cls._instance

    def __init__(self):
        self._conxn = self._instance._conxn

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conxn.close()

    def site_names(self):
        return pandas.read_sql("SELECT NAME FROM SITE", self._conxn)

    def get_results(self, site=None):
        """
        query Manages database by Site

        """

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

        WHERE (name in ({0}))
        """
        if site is not None:
            query = query.format(",".join("?" * len(site)))
            query_params = tuple(_flatten(site))

        else:
            all_sites = self.site_names()["NAME"]
            query = query.format(",".join("?" * len(all_sites)))
            query_params = tuple(_flatten(all_sites))

        return pandas.read_sql(query, self._conxn, params=query_params)
