import seaborn as sns
import matplotlib.pyplot as plt


def boxplot(df, wells, analytes):
    """
    boxplot
    
    Parameters
	----------
	df : pandas DataFrame
	    pandas DataFrame of environmental data 
    
    wells : list of wells to plots
    
    analytes : list of wells to plots
    
    Returns
    -------
    boxplot : boxplot 
        returns a seaborn boxplot.

	Examples
	--------
	>>> from enviropy.plots import boxplot
	>>> boxplot(df, wells, analytes)
    """

    data = df[df.location_id.isin(wells) & df.param_name.isin(analytes)]
    g = sns.factorplot(
        x="location_id",
        y="analysis_result",
        col="param_name",
        data=data,
        kind="box",
        sharey=False,
        sharex=False,
    )
    g.set_titles("{col_name}")
    g.set(xlabel="Location ID", ylabel="Analysis Result")
    plt.show()
