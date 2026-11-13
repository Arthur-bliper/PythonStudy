# s = input()
#
# a = list(s)
#
# b = max(a)
# c = a.count(b)
#
# print(b, c)


s = input()
char_set = set(s)

freq = {c: s.count(c) for c in char_set}

max_char = max(freq)
print(max_char, freq[max_char])
