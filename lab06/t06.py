s = input()
new_s = ""
for ch in s:
    if ch.isalnum() or ch.isspace():
        new_s += ch



lst = new_s.split()

print(len(lst))