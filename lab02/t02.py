n = int(input())

so = n // 100
de = (n // 10) % 10
od = n % 10

a = so == 2 or de == 2 or od == 2
print(a)

b = so % 2 == 0 and de % 2 == 0 and od % 2 == 0
print(b)

c = so + de + od == 18
print(c)
