for _ in range(int(input())):
    w, x, y, z = map(int, input().split())
    if w+y*z == x:
        print('FILLED')
    elif w+y*z > x:
        print('OVERFLOW')
    else:
        print('UNFILLED')