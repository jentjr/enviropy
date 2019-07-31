import numpy as np
from numpy.testing import assert_approx_equal
from enviropy.stats import prediction_interval


def test_two_sided_prediction_interval():
    lpl, upl = prediction_interval(
        [10.0, 11.5, 11.0, 10.6, 10.9, 12.0, 11.3, 10.7], alpha=0.05, type="two-sided"
    )
    assert_approx_equal(lpl, 9.471463, significant=7)
    assert_approx_equal(upl, 12.528537, significant=7)


def test_lower_prediction_interval():
    lpl, upl = prediction_interval(
        [10.0, 11.5, 11.0, 10.6, 10.9, 12.0, 11.3, 10.7], alpha=0.05, type="lower"
    )
    assert_approx_equal(lpl, 9.775309, significant=7)
    assert_approx_equal(upl, np.Inf)


def test_upper_prediction_interval():
    lpl, upl = prediction_interval(
        [10.0, 11.5, 11.0, 10.6, 10.9, 12.0, 11.3, 10.7], alpha=0.05, type="upper"
    )
    assert_approx_equal(lpl, np.NINF)
    assert_approx_equal(upl, 12.22469, significant=7)


def test_k_future_obs():
    lpl, upl = prediction_interval(
        [10.0, 11.5, 11.0, 10.6, 10.9, 12.0, 11.3, 10.7],
        alpha=0.05,
        type="upper",
        k_future_obs=10,
    )
    assert_approx_equal(lpl, np.NINF)
    assert_approx_equal(upl, 13.26213, significant=7)
