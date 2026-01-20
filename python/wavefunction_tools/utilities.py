def alternating_sign(exponent: int) -> int:
    """Return (-1)^m for integer m."""
    # return pow((-1), exponent)
    return 1 if (exponent % 2 == 0) else -1


def condon_shortley_phase_factor(m: int) -> int:
    """Condon-Shortley phase factor: (-1)^m."""
    return alternating_sign(m)


def binomial(n: float, k: int) -> float:
    """
    Generalized Binomial Coefficient - Multiplicative Formula
    C(n, k) for real n and integer k >= 0
    """
    product = 1
    for i in range(1, k + 1):
        product *= (n + 1 - i) / i
    return product
