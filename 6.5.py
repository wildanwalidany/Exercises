from sage.all import *

# a
p = 7
a = 3
b = 2
E = EllipticCurve(GF(p), [a, b])

orderA = E.order()
PointsA = E.points()

print(f"(a) Order of E: {orderA}, Points: {PointsA}")

# b
p = 11
a = 2
b = 7
E = EllipticCurve(GF(p), [a, b])

orderB = E.order()
PointsB = E.points()

print(f"(b) Order of E: {orderB}, Points: {PointsB}")

# c
p = 11
a = 4
b = 5
E = EllipticCurve(GF(p), [a, b])

orderC = E.order()
PointsC = E.points()

print(f"(c) Order of E: {orderC}, Points: {PointsC}")

# d
p = 11
a = 9
b = 5
E = EllipticCurve(GF(p), [a, b])

orderD = E.order()
PointsD = E.points()

print(f"(d) Order of E: {orderD}, Points: {PointsD}")

# e
p = 13
a = 9
b = 5

E = EllipticCurve(GF(p), [a, b])

orderE = E.order()
PointsE = E.points()

print(f"(e) Order of E: {orderE}, Points: {PointsE}")


