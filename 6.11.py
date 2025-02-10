from sage.all import *

# a
p = 83
E = EllipticCurve(GF(p), [23, 13])
P = E(24,14)
n = 19

Ra = n*P
print(f"Ra = {Ra.xy()}")

# b
p = 613
E = EllipticCurve(GF(p), [143, 367])
P = E(195,9)
n = 23

Rb = n*P
print(f"Rb = {Rb.xy()}")

# c
p = 1999
E = EllipticCurve(GF(p), [1828, 1675])
P = E(1756, 348)
n = 11

Rc = n*P
print(f"Rc = {Rc.xy()}")

#d 
p = 3221
E = EllipticCurve(GF(p), [1541, 1335])
P = E(2898, 439)
n = 3211

Rd = n*P
print(f"Rd = {Rd.xy()}")