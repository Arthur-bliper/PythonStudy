def nsd(n, m):

    if m>n:
        n,m = m,n

    if m>n:
        return nsd(m,n)

    while m != 0:
        k = n % m
        n, m = m, k
    return n
# n  m    k
# 12 15
# 15 12
# 15%12 = 3
# 12% 3 = 0
# 3 % 0 !

###### Main ######
a,b = [int(x) for x in input().split()]
print(nsd(a,b))