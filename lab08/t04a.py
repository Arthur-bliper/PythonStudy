# "a" ""

def is_symmetric(s: str):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_symmetric(s[1:-1])

print(is_symmetric("aqbra"))