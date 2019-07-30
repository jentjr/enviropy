import numpy as np
from scipy import stats

__all__ = ["prediction_interval"]


def prediction_interval(x, alpha, type="two-sided"):
    """Compute an interval to contain future measurements with given confidence
    
    Parameters
    ----------
    x : array_like
        Input array or object that can be converted to an array.
    alpha : float
        Type I error rate. Default value is 0.05
    type : string
        The type of interval to be returned. Upper, lower, or two-sided. Default is two-sided.
        
    Returns
    -------
    
    """

    if not isinstance(x, np.ndarray):
        x = np.asarray(x)

    if type == "two-sided":
        lpl = x.mean() - stats.tstd(x) * stats.t.ppf(
            1 - alpha / 2, x.size - 1
        ) * np.sqrt(1 + 1 / x.size)
        upl = x.mean() + stats.tstd(x) * stats.t.ppf(
            1 - alpha / 2, x.size - 1
        ) * np.sqrt(1 + 1 / x.size)

    if type == "upper":
        lpl = np.NINF
        upl = x.mean() + stats.tstd(x) * stats.t.ppf(1 - alpha, x.size - 1) * np.sqrt(
            1 + 1 / x.size
        )

    if type == "lower":
        lpl = x.mean() - stats.tstd(x) * stats.t.ppf(1 - alpha, x.size - 1) * np.sqrt(
            1 + 1 / x.size
        )
        upl = np.Inf

    return lpl, upl
