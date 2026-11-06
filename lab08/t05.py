def nsd(n, m):

    if m>n:
        return nsd(m,n)

    if m == 0:
        return n

    return nsd(m, n % m)

# n      m    k
# 12     15
# 15 <=> 12
# 15  %  12 = 3
# 12  %   3 = 0
# 3   %   0 !

###### Main ######
a,b = [int(x) for x in input().split()]
print(nsd(a,b))
