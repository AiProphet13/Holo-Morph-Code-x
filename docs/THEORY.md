# Holo morp code x: Phase-Lock Protocol - Theory

## Holomorphic Rigidity
The system leverages holomorphic functions to ensure stable bit extraction. 
The squaring operation \( R = R^2 \) maps bits to the complex plane, with topological separation:
- Bit 0: \( \{ z \mid \text{Re}(z) \geq 0 \} \)
- Bit 1: \( \{ z \mid \text{Re}(z) < 0 \} \)

## Phase Wrap-Around Immunity
Direct phase computation is avoided to prevent discontinuities at \( \pm \pi \). 
Instead, real and imaginary checks ensure robust decision boundaries.

## Basin Convergence
The decoder verifies convergence to the target \( T \) within \( \epsilon = 10^{-8} \), with error bound:
\[ \Delta_k \leq \kappa \epsilon_{\text{machine}} \frac{|T|^{2^k}}{1 - |T|} \]
