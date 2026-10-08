n = int(input())

result = 0

for number in range(10, 100):
    first_digit = number // 10
    last_digit = number % 10

    if n == 1 and first_digit > last_digit:
        result = result + 1

    elif n == 2 and first_digit < last_digit:
        result += 1

    elif n == 3 and first_digit % 2 - last_digit % 2 == 0:
        result += 1

    elif n == 4 and first_digit == last_digit:
        result += number

    elif n == 5 and first_digit % 2 + last_digit % 2 == 0:
        result += number

    elif n == 6 and first_digit % 2 + last_digit % 2 == 2:
        result += number
        
print(result)
