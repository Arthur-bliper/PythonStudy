lst = [int(el) for el in input()]

result = [0] * 10
# 0 1 2 3 4 5 6 7 8 9

for i in range(10):
    result[i] = lst.count(i)

print(*result)



