n = int(input())

lst = []

for i in range(n):
    new = int(input())
    lst.append(new)

for i in range(n//2):
    lst[i], lst[n-1-i] = lst[n-1-i], lst[i]

print(*lst)

