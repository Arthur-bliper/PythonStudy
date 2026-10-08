while True:
    n = int(input())
    # n = 2 [10,99]  [10**(n-1), 10**n-1]

    result = 0

    for i in range(10**(n-1),10**n):
        if i%2==0:
            result +=1

    print(result)