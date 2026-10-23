def is_prime(k):
    if k==1:
        return False
    for i in range(2,k):
        if k%i==0:
            return False
    return True

def rev(k) -> int:
    inverted = 0
    while k>0:
        last_digit = k%10
        inverted = inverted * 10 + last_digit
        k = k//10
    return inverted


###### Main ######
a,b = [int(x) for x in input().split()]
count = 0
for num in range(a, b+1):
    if is_prime(num) and is_prime(rev(num)):
        count +=1
print(count)
