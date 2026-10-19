s = input()

new_s = s[0]
for ch in s[1:]:
    if not(ch == " " and new_s[-1] == " "):
        new_s += ch
print(new_s.strip())