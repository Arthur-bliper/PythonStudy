_ = int(input())
lst = [int(i) for i in input().split()]

print(lst)
for el in lst:
    if el >= 0:
        el = el + 2
    print(el, end=" ")
print()
print(lst)

# el = lst[0]
# el = lst[1]
# el = lst[2]
# el = lst[3]