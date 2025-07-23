import cmath
import numpy as np

# TOLERANCE PROFILE (optimized for 256-bit fidelity)
PHASE_TOL = 1e-12  # Boundary stability threshold
REAL_TOL = 1e-15   # Floating-point noise immunity
ATTRACTOR_ε = 1e-8  # Final basin convergence check

class HolomorphicIntegrityError(Exception):
    """Custom exception for basin divergence."""
    pass

def holomorphic_decode_fixed(P_k: complex, T: float, depth: int) -> list[int]:
    """Fixed decoder with holomorphic basin locking."""
    R = P_k
    bits = []
    
    for _ in range(depth):
        # --- PHASE-LOCK CORE (3-layer stability) ---
        real, imag = R.real, R.imag
        
        # 1. REAL-ANCHORED DECISION (avoid phase jumps)
        if abs(real) > REAL_TOL:
            bit = 0 if real > 0 else 1
        # 2. IMAGINARY TIEBREAKER (|Re| < ε edge case)
        elif imag >= PHASE_TOL:
            bit = 0
        elif imag <= -PHASE_TOL:
            bit = 1
        # 3. SINGULARITY GUARD (theoretical impossibility)
        else:
            bit = int(np.sign(cmath.phase(R)))  # Fallback
            
        bits.append(bit)
        R = R**2  # Forward iterate
    
    # --- BASIN CONVERGENCE VERIFICATION ---
    if abs(R - T) > ATTRACTOR_ε:
        raise HolomorphicIntegrityError(
            f"Basin divergence: |R - T| = {abs(R - T)} > ε"
        )
    
    return bits[::-1]  # Original bit order
