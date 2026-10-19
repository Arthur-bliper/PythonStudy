s = input()
new_s = s[0]
for ch in s[1:]:
    if ch != new_s[-1]:
        new_s += ch
print(new_s)