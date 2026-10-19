while True:
    try:
        words = input().split()
    except EOFError:
        break
    for word in words:
        print(len(word), end=" ")
