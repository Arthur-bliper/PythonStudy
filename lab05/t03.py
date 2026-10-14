n = int(input())
lst = [float(i) for i in input().split()]

count = 0
suma = 0
#
# for i in range(n):
#     if lst[i] > 0 and (i+1)%3 ==0:
#         count += 1
#         suma += lst[i]

for el in lst[2::3]:
    if el>0:
        suma += el
        count += 1
print(f"{count} {suma:.2f}")

# a = list(range(15))
# print(a)
# print(a[2::3])
