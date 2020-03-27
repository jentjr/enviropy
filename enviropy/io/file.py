import pandas as pd
from enviropy import Enviropy

def read_csv(fname):
    df = pd.read_csv(fname)
    return Enviropy(df)