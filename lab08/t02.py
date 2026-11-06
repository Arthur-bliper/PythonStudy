#             / 0, n==0
# mult(n,m) = {
#             \ mult(n-1,m) + m

def mult(m,n):
    if n==0:
        return 0

    return mult(n-1,m) + m

########## MAIN ##########
print(mult(5,3))