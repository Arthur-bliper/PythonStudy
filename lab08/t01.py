# 5! = 4! * 5
#      ||
#      3! * 4
#      ||
#      2! * 3
#      ||
#      1! * 2
#      ||
#      0! * 1
#      ||
#      1

def fact(n):
    if n==0:
        return 1
    else:
        f = fact(n-1)
        res = n * f
        return res

########## MAIN ##########
print(fact(5))