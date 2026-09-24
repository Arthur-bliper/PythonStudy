n=int(input())
a = n%2 != 0

b = 99 < n < 1000

cond  = a or b

answer = "YES" if cond else "NO"

print(answer)