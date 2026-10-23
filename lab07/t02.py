# a) повними квадратами;
def is_square(k):
    return int(k**0.5)**2 == k
# b) степенями п’ятірки;
def is_pow5(k):
    while k>1:
        if k%5 != 0:
            return False
        k=k//5
    return True
# c) простими числами.
def is_prime(k):
    if k==1:
        return False
    for i in range(2,k):
        if k%i==0:
            return False
    return True

###### Main ######
n = int(input())

squares = []
powers_of_five = []
primes = []

for _ in range(n):
    new_num = int(input())
    if is_square(new_num):
        squares.append(new_num)
    if is_pow5(new_num):
        powers_of_five.append(new_num)
    if is_prime(new_num):
        primes.append(new_num)

print("Квадрати",*squares)
print("Степені 5",*powers_of_five)
print("Прості числа",primes)