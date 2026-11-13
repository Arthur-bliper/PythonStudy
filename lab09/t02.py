n = int(input())
number_lst = [int(i) for i in input().split()]

freq = dict()
for num in number_lst:
    # if num not in freq:
    #     freq[num] = 1
    # else:
    #     freq[num] = freq[num] + 1
    freq[num] = freq.get(num, 0) + 1

# print(freq)
n_2 = n//2
for key, value in freq.items():
    if value > n_2:
        print(key)
        break
else:
    print(-1)