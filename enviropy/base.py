import pandas
from enviropy.plots import EnviroPlot

class EnviroData(EnviroPlot):
    def __init__(self, df):
        self.df = df
