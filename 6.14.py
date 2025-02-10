from sage.all import *

p = 2671
E = EllipticCurve(GF(p), [171, 853])
P = E(1980, 431)

# (a)
QA = E(2110, 543)
nB = 1943

QB = nB*P
print(f"QB = {QB.xy()}")

# (b)
shared_secret = nB*QA
print(f"Shared secret: {shared_secret.xy()[0]}")

# (c)
# nA = 2045
P_order = P.order()
nA = QA.log(P)
print(f"Order of P: {P_order} and nA: {nA}")

# (d)
xA = 2
nB = 875

xB = nB*P[0]
QA = E.lift_x(Integer(xA))
shared_secret = nB*QA
print(f"xB = {xB} and shared secret: {shared_secret.xy()[0]}")

