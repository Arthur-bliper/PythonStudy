# 4! = 1 * 2 * 3 * 4

# 0! = 1
# 1! = 0! * 1
# 2! = 1! * 2
# 3! = 2! * 3
# 4! = 3! * 4

n = 4

fact_n = 1

k = 0

while k < n:
    k = k + 1
    fact_n = fact_n * k

print(fact_n)