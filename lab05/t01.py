_ = int(input())
lst = [int(i) for i in input().split()]

i = 0

# maximum = -101
maximum = lst[0]

# while i < n:
#     if lst[i] > maximum:
#         maximum = lst[i]
#     i = i + 1

# for i in range(n):
#     if lst[i] > maximum:
#         maximum = lst[i]

# for el in lst:
#     if el > maximum:
#         maximum = el

print(max(lst))