import seaborn as sns
import matplotlib.pyplot as plt

class EnviroPlot:
    def boxplot(self, wells, analytes):
        data = self[self.location_id.isin(wells) & self.param_name.isin(analytes)]
        g = sns.factorplot(x="location_id", y="analysis_result", col='param_name',
                data=data, kind="box", sharey=False, sharex=False)
        g.set_titles("{col_name}")
        g.set(xlabel='Location ID', ylabel = 'Analysis Result')
        plt.show()
