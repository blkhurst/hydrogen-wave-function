import pytest
import numpy as np
from numpy.testing import assert_allclose

from scipy.special import assoc_laguerre
from wavefunction_tools import associated_laguerre_polynomial

NK_VALUES = [(0, 0), (1, 0), (1, 2), (2, 0), (2, 3), (5, 0), (5, 2), (10, 0), (10, 4)]
X_SCALAR = [-2, -1e-6, 0.0, 1e-14, 0.1, 1.0, 2.5, 10.0]
X_ARRAY = [np.linspace(-2.0, 10.0, 80)]


@pytest.mark.parametrize("n,k", NK_VALUES)
@pytest.mark.parametrize("x", X_SCALAR + X_ARRAY)
def test_associated_laguerre_matches_scipy(n, k, x):
    expected = assoc_laguerre(x, n, k)
    got = associated_laguerre_polynomial(n, k, x)

    assert_allclose(got, expected, rtol=1e-10, atol=1e-12)
