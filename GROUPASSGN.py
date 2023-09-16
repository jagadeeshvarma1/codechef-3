t = int(input())
while t > 0 :
    n,x = map(int, input().split())
    print((2*n) - x + 1)
    t -= 1