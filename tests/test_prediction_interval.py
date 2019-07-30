import numpy as np
from numpy.testing import assert_allclose
from enviropy.stats import prediction_interval


def test_two_sided_prediction_interval():
    lpl, upl = prediction_interval(
        [10.0, 11.5, 11.0, 10.6, 10.9, 12.0, 11.3, 10.7], alpha=0.05, type="two-sided"
    )
    assert_allclose(lpl, 9.471463)
    assert_allclose(upl, 12.528537)


def test_lower_prediction_interval():
    lpl, upl = prediction_interval(
        [10.0, 11.5, 11.0, 10.6, 10.9, 12.0, 11.3, 10.7], alpha=0.05, type="lower"
    )
    assert_allclose(lpl, 9.775309)
    assert_allclose(upl, np.Inf)


def test_upper_prediction_interval():
    lpl, upl = prediction_interval(
        [10.0, 11.5, 11.0, 10.6, 10.9, 12.0, 11.3, 10.7], alpha=0.05, type="upper"
    )
    assert_allclose(lpl, np.NINF)
    assert_allclose(upl, 12.22469)
