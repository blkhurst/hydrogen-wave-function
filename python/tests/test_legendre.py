import pytest
import numpy as np
from numpy.testing import assert_allclose

from scipy.special import lpmv
from wavefunction_tools import associated_legendre_polynomial


LM_VALUES = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 2), (3, 2), (3, 3), (5, 2), (6, 4)]
LM_VALUES_NEG = [(1, -1), (2, -1), (2, -2), (3, -1), (3, -2), (3, -3), (6, -4)]

X_SCALAR = [-1.0, -0.75, -1e-6, 0.0, 1e-12, 0.2, 0.9, 1.0]
X_ARRAY = [np.linspace(-1.0, 1.0, 200)]


@pytest.mark.parametrize("l,m", LM_VALUES + LM_VALUES_NEG)
@pytest.mark.parametrize("x", X_SCALAR + X_ARRAY)
def test_associated_legendre_matches_scipy(l, m, x):
    # Ensure both implementations include the Condon-Shortley phase factor
    expected = lpmv(m, l, x)
    got = associated_legendre_polynomial(l, m, x)

    assert_allclose(got, expected, rtol=1e-10, atol=1e-12)
