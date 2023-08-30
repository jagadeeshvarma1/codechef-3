for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    if a == b or a == c or a == d:
        print("Yes")
    elif(a == (b+c)) or (a == (d+c)) or (a == (b+d)) or (a == (b+c+d)):
        print("Yes")
    else:
        print("NO")