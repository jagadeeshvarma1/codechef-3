for t in range(int(input())):
    a, b, c, d =input().split()
    a, b, c, d = int(a), int(b), int(c), int(d)
    a = a - c
    b = b - d
    if a < b:
        print("first")
    elif a == b:
        print("any")
    else:
        print("second")