# n = int(input())
# number_set = {int(i) for i in input().split()}
# print(number_set)



# 33333333333333333333333333333333333333333333333333333333333333333 5 -7 7 5 -9 -4
# n = int(input())
# numbers = [int(i) for i in input().split()]
# print(*[x for x in numbers if numbers.count(x) == 1])

n = int(input())
elems = [int(e) for e in input().split()]

elem_set_freq_more_than_one_time = set()

for el in elems:
    if el in elem_set_freq_more_than_one_time:
        continue

    if elems.count(el) == 1:
        print(el, end=" ")
    else:
        elem_set_freq_more_than_one_time.add(el)