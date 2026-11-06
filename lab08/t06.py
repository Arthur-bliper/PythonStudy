# 1 1 2 3 5 8 13 21

def fib1(n):
    if n<=2:
        return 1
    return fib1(n-1)+fib1(n-2)

############## MAIN ###############
# print(fib1(39))
k = int(input())
for _ in range(k):
    num = int(input())
    print(fib1(num))