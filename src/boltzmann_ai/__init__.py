"""Reference tools for rarefied gas dynamics."""

from math import exp, isfinite, pi, sqrt


def maxwellian_1d(c: float) -> float:
    """Return the probability density of one standardized velocity component.

    c = (v - u) / sqrt(k_B T / m). The area under this density is one.
    """
    if not isfinite(c):
        raise ValueError("c must be finite")
    return exp(-0.5 * c * c) / sqrt(2.0 * pi)
