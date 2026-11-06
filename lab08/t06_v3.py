#       a b
# 1 1 2 3 5 8 13 21

def fib2(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
    return a

############## MAIN ###############
# print(fib1(39))
k = int(input())
for _ in range(k):
    num = int(input())
    print(fib2(num))