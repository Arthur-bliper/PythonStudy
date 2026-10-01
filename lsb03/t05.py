# 12345

n = int(input())

digit_sum = 0
digit_dob = 1

print(digit_dob, digit_sum)

while n>0:
    last_digit = n %10
    digit_sum = digit_sum + last_digit
    digit_dob = digit_dob * last_digit
    print(last_digit)
    n = n // 10
print(f"{digit_dob/digit_sum:.3f}")

