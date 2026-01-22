import pytest
import numpy as np
from numpy.testing import assert_allclose
from scipy.special import eval_genlaguerre
from math import factorial

from wavefunction_tools import radial_wave_function, radial_distribution
from wavefunction_tools.utilities import a0, Z


NL_VALUES = [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1), (4, 2), (4, 3)]

R_SCALAR = [0.0, 1e-14, 1e-10, 1e-6, 0.1, 0.5, 1.0, 2.0, 10.0, 30.0]
R_ARRAY = [np.linspace(0.0, 40.0, 400)]


def _radial_wave_function_scipy(n: int, l: int, r):
    """Radial wave function R_{nl}(r) using scipy.special.eval_genlaguerre for testing"""
    r = np.asarray(r, dtype=float)
    norm = np.sqrt(
        ((2.0 * Z) / (n * a0)) ** 3
        * (factorial(n - l - 1) / (2.0 * n * factorial(n + l)))
    )
    rho = (2.0 * Z * r) / (n * a0)
    L = eval_genlaguerre(n - l - 1, 2 * l + 1, rho)
    return norm * np.exp(-rho / 2.0) * (rho**l) * L


@pytest.mark.parametrize("n,l", NL_VALUES)
@pytest.mark.parametrize("r", R_SCALAR + R_ARRAY)
def test_radial_wave_function_matches_scipy(n, l, r):
    expected = _radial_wave_function_scipy(n, l, r)
    got = radial_wave_function(n, l, r)

    assert_allclose(got, expected, rtol=1e-10, atol=1e-12)


@pytest.mark.parametrize("n,l", NL_VALUES)
def test_radial_distribution_is_normalized(n, l):
    r_max = 80.0 * n * a0 / Z
    r = np.linspace(0.0, r_max, 8000)

    # Assumes Spherical Harmonics normalised to 1,
    # meaning no numerical integration normalisation required
    P = radial_distribution(n, l, r)
    integral = np.trapezoid(P, r)

    assert_allclose(integral, 1.0, rtol=1e-6, atol=1e-8)
