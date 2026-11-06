# 1011(10)  = 1 * 10 ** 3 +
#             0 * 10 ** 2 +
#             1 * 10 ** 1 +
#             1 * 10 ** 0 +

# 1011(2)  = 1 * 2 ** 3 +
#            0 * 2 ** 2 +
#            1 * 2 ** 1 +
#            1 * 2 ** 0 = 8 + 0 + 2 + 1 = 11(10)

# 1011 % 10 = 1,  1 * 2 ** 0 = 1,  1011 // 10 = 101
# 101  % 10 = 1,  1 * 2 ** 1 = 2,  101  // 10 = 10
# 10   % 10 = 0,  0 * 2 ** 2 = 0,  10   // 10 = 1
# 1    % 10 = 1,  1 * 2 ** 3 = 8,  1    // 10 = 0

def bin_to_dec(n):
    result = 0
    power = 0
    while n > 0:
        digit = n % 10
        result = result + digit * 2 ** power
        n = n // 10
        power += 1

    return result

# 29 - 16 * 1 = 13
# 13 - 8  * 1 = 5
# 5  - 4  * 1 = 1
# 1  - 2  * 0 = 1
# 1  - 1  * 1 = 0

# 29 % 2 = 1,  1 * 10 ** 0 = 1,      29 // 2 = 14
# 14 % 2 = 0,  0 * 10 ** 1 = 0,      14 // 2 = 7
# 7  % 2 = 1,  1 * 10 ** 2 = 100,    7  // 2 = 3
# 3  % 2 = 1,  1 * 10 ** 3 = 1000,   3  // 2 = 1
# 1  % 2 = 1,  1 * 10 ** 4 = 10000,  1  // 2 = 0

def dec_to_bin(n):
    result = 0
    power = 0
    while n > 0:
        digit = n % 2
        result = result + digit * 10 ** power
        n = n // 2
        power += 1

    return result

###### Main ######
a = int(input())
b = int(input())

a = bin_to_dec(a)
b = bin_to_dec(b)

print(dec_to_bin(a + b))

