import numpy as np
from scipy import stats

__all__ = ["prediction_interval"]


def prediction_interval(x, alpha=0.05, type="two-sided", k_future_obs=1):
    """Compute an interval to contain future measurements with given confidence
    
    Parameters
    ----------
    x : array_like
        Input array or object that can be converted to an array.
    alpha : float
        Individual comparison false positive rate. Default value is 0.05.
    type : string
        The type of interval to be returned. Upper, lower, or two-sided. Default is two-sided.
    k_future_obs: int
        Number of total future comparisons(e.g., number of wells multiplied by the number of analytes).
        
    Returns
    -------
    
    Notes
    -----
    
    Uses Bonferroni inequality method. 
    
    """

    if not isinstance(x, np.ndarray):
        x = np.asarray(x)

    alpha_s = alpha

    if k_future_obs > 1:
        alpha = alpha_s / k_future_obs

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
