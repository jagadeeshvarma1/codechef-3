for i in range(int(input())):
    a,b,x,y=map(int,input().split())
    if (a>b):
        z=a-b
        if(y>=z):
            print("YES")
        else:
            print("NO")
    elif b>a:
        z=b-a
        if(x>=z):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")