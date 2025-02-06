from sage.all import *

# Define the finite field
p = 5

# Define the elliptic curve
E = EllipticCurve(GF(p), [1, 1])

# Define the points P and Q
P = E(4, 2)
Q = E(0, 1)

# Solve for n such that Q = nP
n = Q.log(P)

print(f"The value of n such that Q = nP is: {n}")
