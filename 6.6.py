from sage.all import *
from tabulate import tabulate

# a
print("(a)")
# Define the finite field and elliptic curve parameters
p = 5
a = 1
b = 2

# Define the elliptic curve E over GF(p)
E = EllipticCurve(GF(p), [a, b])

# List all points on the elliptic curve E
points = E.points()
print(f"E(F5) = {points}")

table = []

for x in points:
    row = [x]
    for y in points:
        row.append(x+y)
    table.append(row)

# Print the table using tabulate
headers = ["+"] + points
print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

