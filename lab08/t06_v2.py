# 1 1 2 3 5 8 13 21

fibs = [0, 1, 1]

def fib3(n):
    global fibs
    if n < len(fibs):
        return fibs[n]

    fib = fib3(n-1)+fib3(n-2)
    fibs.append(fib)
    return fib

############## MAIN ####
# print(fib3(100))
k = int(input())
for _ in range(k):
    num = int(input())
    print(fib3(num))
