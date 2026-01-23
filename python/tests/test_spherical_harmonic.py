import pytest
import numpy as np
from numpy.testing import assert_allclose

from scipy.special import sph_harm_y
from wavefunction_tools import spherical_harmonic

# Ensure positive, negative, even, odd m values are all tested
LM_VALUES = [
    (0, 0),
    (1, 0),
    (1, 1),
    (1, -1),
    (2, 0),
    (2, 1),
    (2, -1),
    (2, 2),
    (2, -2),
    (3, 0),
    (3, 1),
    (3, -1),
    (3, 2),
    (3, -2),
    (3, 3),
    (3, -3),
    (4, 1),
    (4, -1),
    (4, 2),
    (4, -2),
    (4, 3),
    (4, -3),
    (4, 4),
    (4, -4),
    (6, 4),
    (6, -4),
]

THETA_SCALAR = [0.0, 1e-12, 0.2, 1.0, np.pi / 2, np.pi - 1e-12]  # [0, pi]
PHI_SCALAR = [0.0, 1e-12, 1.0, np.pi, 2 * np.pi - 1e-12]  # [0, 2pi]


@pytest.mark.parametrize("l,m", LM_VALUES)
@pytest.mark.parametrize("theta", THETA_SCALAR)
@pytest.mark.parametrize("phi", PHI_SCALAR)
def test_spherical_harmonic_matches_scipy(l, m, theta, phi):
    """
    Verifies Condon-Shortley phase / sign conventions are implemented correctly.
    Ensure polar and azimuthal angle conventions match (scipy.special.sph_harm_y updated in 1.15.0).
    """
    expected = sph_harm_y(l, m, theta, phi)  # complex
    re, im = spherical_harmonic(l, m, theta, phi)
    got = re + 1j * im

    assert_allclose(got, expected, rtol=1e-10, atol=1e-11)
