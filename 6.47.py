from sage.all import *

p = 1723
E = EllipticCurve(GF(p), [1, 0])
P = E(668,995)

assert P.order() == 431
print(f"Order of P: {P.order()}")