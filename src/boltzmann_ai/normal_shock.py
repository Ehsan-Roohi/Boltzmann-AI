"""Ideal-gas normal shock relation from FlowMLLab (see third-party/FlowMLLab-LICENSE)."""

import math

GAMMA = 1.4


def normal_shock_downstream_mach(mach_upstream: float, gamma: float = GAMMA) -> float:
    """Return the downstream Mach number of a normal shock."""
    m1 = float(mach_upstream)
    if m1 <= 1.0:
        raise ValueError("Normal-shock upstream Mach number must exceed one.")
    return math.sqrt(
        (1.0 + 0.5 * (gamma - 1.0) * m1**2)
        / (gamma * m1**2 - 0.5 * (gamma - 1.0))
    )
