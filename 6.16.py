# b
p = 1123
a = 54
b = 87
xA = 278
Beta = 0

u = (xA**3 + a*xA + b) % p
print(f"u = {u}")

y1 = pow(u, (p+1)//4, p)
y2 = p - y1
print(f"y1 = {y1} and y2 = {y2}")

if y1<y2 and Beta == 0:
    y = y1
else:
    y = y2
    
print(f"The chosen y is {y}")