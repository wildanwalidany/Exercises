from sage.all import *
from tabulate import tabulate

primes = [3, 5, 7, 11, 13, 17]

cardinality = []
tp = []
hasse_bound = []

for p in primes:
    curve = EllipticCurve(GF(p), [1, 1])
    n = curve.cardinality()
    cardinality.append(n)
    tp.append(p + 1 - n)
    hasse_bound.append(2 * sqrt(p).n(prec=13))

table = zip(primes, cardinality, tp, hasse_bound)
headers = ["Prime", "#E(Fp)", "tp", "Hasse's bound"]

print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
