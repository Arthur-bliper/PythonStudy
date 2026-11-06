# ""
def inv(s: str) -> str:
    if s == "":
        return s
    return s[-1] + inv(s[:-1])

print(inv("1234567890"))