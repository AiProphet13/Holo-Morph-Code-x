import cmath
import numpy as np

def phase_check(z: complex) -> float:
    """Safe phase computation with boundary protection."""
    if abs(z.real) < 1e-15 and abs(z.imag) < 1e-15:
        return 0.0
    return cmath.phase(z)
