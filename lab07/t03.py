def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b
def min_of_2(a, b):
    if a < b:
        return a
    else:
        return b
def min_of_3(a, b, c):
    return min_of_2(a,min_of_2(b,c))

x, y, z = [float(d) for d in input().split()]
print(min_of_3(max_of_2(x, y), max_of_2(y, z), x + y + z))