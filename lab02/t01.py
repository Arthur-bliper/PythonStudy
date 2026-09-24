n = int(input())

a = n %2 ==0
print(a)

b = n % 10 == 0
print(b)

de = n//10
od = n % 10
c = de+od > 9
print(c)