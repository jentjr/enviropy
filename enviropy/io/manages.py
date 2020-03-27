import pyodbc
import pandas as pd
from enviropy import Enviropy

__all__ = ["read_manages3", "read_manages4"]


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
    >>> from enviropy.io import read_manages3
    >>> data = read_manages3('C:\Path\to\Site.mdb')
    """

    driver = "{Microsoft Access Driver (*.mdb, *.accdb)}"
    database = mdb_path

    con = pyodbc.connect("DRIVER={0};DBQ={1}".format(driver, database))

    query = """
    SELECT sample_results.location_id,
    sample_results.sample_date, site_parameters.param_name,
    sample_results.lt_measure, sample_results.analysis_result,
    site_parameters.default_unit
    FROM sample_results LEFT JOIN site_parameters
    ON sample_results.storet_code = site_parameters.storet_code
    """

    df = pd.read_sql(query, con)

    con.close()

    return Enviropy(df)


def read_manages4(sql, con):
    """
    Function to read a MANAGES 4.x database and return
    the data in a pandas DataFrame for analysis.
    
    Parameters
    ----------
    sql : str
        SQL query to execute.
    con : DB connection or SQAlchemy engine
        Active connection to teh databse to query
        
    Returns
    -------
    Enviropy DataFrame
    
    Examples
    --------
    >>> sql =  "
    SELECT sample_results.location_id,
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
    "
    >>> from enviropy.io import read_manages_4
    >>> 
    """

    df = pandas.read_sql(sql, con)
    
    return Enviropy(df)