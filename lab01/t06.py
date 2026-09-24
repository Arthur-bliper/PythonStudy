a = input().split()
x = float(a[0])
y = float(a[1])

z = (2 * x ** 2
     - 4 * x * y
     + 3 * y ** 2
     + (x + y) / 7)

print(f"{z:.3f}")
