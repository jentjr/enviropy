import enviropy.io
import pandas as pd


class Enviropy(pd.DataFrame):
    """Class for environmental statistics DataFrame
    
    Parameters
    ----------
    location_id: str
        sampling location
    sample_date: date
        sampling date
    param_name: str
        name of constituent, or analyte
    analysis_result: int or float
        sample result
    detection_limit: int or float
        method detection limit
    reporting_limit: int or float
        lab reporting limit
    qualifier_flag: str
        qualifier flags such as J, or U for non-detects
    measure_unit: str
        unit of measurement
    
    """
    
    @property
    def _constructor(self):
        return Enviropy
    
    @classmethod
    def from_manages3(cls, mdb_path):
        return enviropy.io.manages.read_manages3(mdb_path)
    
    @classmethod
    def from_manages4(cls, sql, con):
        return enviropy.io.manages.read_manages4(sql, con)
    
    @classmethod
    def from_csv(cls, fname):
        return enviropy.io.file.read_csv(fname)
        