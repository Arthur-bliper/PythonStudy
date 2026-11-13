# a = input()
# b = input()
# list1 = list(a)
# list2 = list(b)
# lset = set(list1)
# c = 0
# for l in lset:
#     if list1.count(l) < list2.count(l):
#         print("No")
#         break
# else:
#     print("Ok")

donor = input()
recipient = input()

freq_donor = {c: donor.count(c) for c in donor}
freq_recipient = {c: recipient.count(c) for c in recipient}

# print(freq_donor)
# print(freq_recipient)

for ch, count in freq_recipient.items():
    if count > freq_donor.get(ch, 0):
        print("No")
        break
else:
    print("Ok")
