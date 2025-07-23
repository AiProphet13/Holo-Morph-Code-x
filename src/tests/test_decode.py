import pytest
from src.core.holomorphic_decode import holomorphic_decode_fixed, HolomorphicIntegrityError

def test_basic_decode():
    P_k = 0.707j
    T = 0.5
    depth = 3
    expected = [1, 0, 1]
    result = holomorphic_decode_fixed(P_k, T, depth)
    assert result == expected, f"Expected {expected}, got {result}"

def test_basin_divergence():
    with pytest.raises(HolomorphicIntegrityError):
        holomorphic_decode_fixed(0.707j, 10.0, 3)  # Invalid T
