import pyodbc
import pandas

def read_manages3(mdb_path):
    """
	Function to read MANAGES 3.X database and return
	groundwater data in Pandas DataFrame for analysis.

	Parameters
	----------
	mdb_path : connection string
	    The path to the MANAGES 3.x Site.mdb file.

    Returns
    -------
    DataFrame :  pandas DataFrame
        returns a pandas DataFrame.

	Examples
	--------
	>>> from enviropy.external import read_manages3
	>>> cd = manages.read_manages3('H:\INTERNAL\MANAGES_DATA\Cardinal\Cardinal\Site.mdb')

    .. autoclass:: read_manages3

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
	
def read_gint(gpj_path):
    """
	Function to read gINT database and return
	boring log data and well construction details 
	in Pandas DataFrame for analysis.
	
	Parameters
	----------
	gpj_path : connection string
	    The path to the MANAGES 3.x Site.mdb file.

    Returns
    -------
    DataFrame :  pandas DataFrame
        returns a pandas DataFrame.

	Examples
	--------
	>>> from enviropy.external import read_gint
	>>> cd = gint.read_gint('L:\Internal\gINTw\CD far ccr project.gpj')

    .. autoclass:: read_gint

	"""

    driver = '{Microsoft Access Driver (*.mdb, *.accdb)}'
    database = gpj_path

    conxn = pyodbc.connect('DRIVER={0};DBQ={1}'.format(driver, database))

    query = """

    SELECT MON_WELL_CONSTR.Mon_Well_Number, MON_WELL_CONSTR.Type_Grout,
	MON_WELL_CONSTR.Type_Bent, MON_WELL_CONSTR.Type_Screen,
	MON_WELL_CONSTR.Dia_Screen, MON_WELL_CONSTR.Length_Screen,
	MON_WELL_CONSTR.Type_Gravel, MON_WELL_CONSTR.Type_Riser, 
	MON_WELL_CONSTR.Dia_Riser, MON_WELL_CONSTR.Spacer_Depths,
	MON_WELL_CONSTR.Comments, MON_WELL_CONSTR.Top_Bent_Depth,
	MON_WELL_CONSTR.Top_Gravel_Depth, MON_WELL_CONSTR.Check_Valve_Depth,
	MON_WELL_CONSTR.Bot_Well_Depth, MON_WELL_CONSTR.Bot_Gravel_Depth,
	LITHOLOGY.Depth, LITHOLOGY.Bottom, LITHOLOGY.Graphic, LITHOLOGY.Description
	FROM LITHOLOGY LEFT JOIN MON_WELL_CONSTR ON
	MON_WELL_CONSTR.PointID = LITHOLOGY.PointID

    """

    data = pandas.read_sql(query, conxn)

    conxn.close()

    return data