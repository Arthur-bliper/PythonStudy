# 12345

n = int(input())

digit_count = 0 if n>0 else 1

while n>0:
    digit_count = digit_count +1
    n = n // 10
print(digit_count)