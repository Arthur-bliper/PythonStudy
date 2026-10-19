s = input()
count = 0
for ch in s[1:]:
    # if ch == '+' or ch == '-' or ch == '*':
    #     count += 1
    if ch in '+-*':
        count += 1
print(count)