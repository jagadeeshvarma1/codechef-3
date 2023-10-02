t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if(y==0):
        print(x)
    elif x>y:
        print(x+y)
    else:
        print((x+y)-1)