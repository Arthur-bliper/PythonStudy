x1, y1, x2, y2, x3, y3 = [float(d) for d in input().split()]
print(x1, y1, x2, y2, x3, y3)

l1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
l2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** (1 / 2)
l3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** (1 / 2)
per = l1 + l2 + l3
p = per / 2
s = (p * (p - l1) * (p - l2) * (p - l3)) ** 0.5
print(per, s)
print(f"{per:0.4f} {s:0.4f}")
