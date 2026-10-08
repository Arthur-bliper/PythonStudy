count =0
while True:
    n=int(input())
    if n == 0 :
        break
    elif n%2 == 0:
        continue
    else:
        count = count + 1
print(count)