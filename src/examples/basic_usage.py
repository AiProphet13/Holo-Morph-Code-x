import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.holomorphic_decode import holomorphic_decode_fixed

def main():
    P_k = 0.707j
    T = 0.5
    depth = 3
    bits = holomorphic_decode_fixed(P_k, T, depth)
    print(f"Decoded bits: {bits}")

if __name__ == "__main__":
    main()
