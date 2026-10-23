def is_prime(k):
    if k==1:
        return False
    for i in range(2,k):
        if k%i==0:
            return False
    return True

###### Main ######
n = int(input())

for num  in range(n,2*n-1):
    first = num
    second = num+2

    if is_prime(second) and is_prime(first):
        print(first, second)