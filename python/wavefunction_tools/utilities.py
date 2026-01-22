Z = 1
a0 = 1


def alternating_sign(exponent: int) -> int:
    """Return (-1)^m for integer m."""
    # return pow((-1), exponent)
    return 1 if (exponent % 2 == 0) else -1


def condon_shortley_phase_factor(m: int) -> int:
    """Condon-Shortley phase factor: (-1)^m."""
    return alternating_sign(m)


def factorial_ratio(a: int, b: int) -> float:
    """Return a!/b! for integers 0<=a<=b using a product (avoids factorials)."""
    if a < 0 or b < 0 or a > b:
        raise ValueError("Require 0 <= a <= b")
    prod = 1.0
    for k in range(a + 1, b + 1):
        prod /= k
    return prod


def binomial(n: float, k: int) -> float:
    """
    Generalized Binomial Coefficient - Multiplicative Formula
    C(n, k) for real n and integer k >= 0
    """
    product = 1
    for i in range(1, k + 1):
        product *= (n + 1 - i) / i
    return product
