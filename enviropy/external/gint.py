import pyodbc
import pandas

__all__ = ["read_gint"]


def read_gint(gpj_path):
    """
	Function to read gINT database and return
	boring log data and well construction details
	in Pandas DataFrame for analysis.

	Parameters
	----------
	gpj_path : str
	    The path to the gINT .gpj file.

    Returns
    -------
    DataFrame :  pandas DataFrame
        returns a pandas DataFrame.

	Examples
	--------
	>>> from enviropy.external import read_gint
	>>> cd = read_gint('L:\Internal\gINTw\CD far ccr project.gpj')

	"""

    driver = "{Microsoft Access Driver (*.mdb, *.accdb)}"
    database = gpj_path

    conxn = pyodbc.connect("DRIVER={0};DBQ={1}".format(driver, database))

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
