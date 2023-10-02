t=int(input())
for _ in range(t):
    a,b,c,d,z=list(map(int,input().split()))
    x=a/c
    y=b/d
    e=min(x,y)
    if(e>=z):
        print("YES")
    else:
        print("NO")