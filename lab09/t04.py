n = int(input())
a = [int(i) for i in input().split()]

cnt = dict()
last = dict()

for i in range(len(a)):
    cnt[a[i]] = cnt.get(a[i], 0) + 1
    last[a[i]] = i

res = []
for i, value in enumerate(a):
    if cnt[value] > 1 and last[value] == i:
        res.append(str(value))

if res:
    print(" ".join(res))
else:
    print("NO")