t=int(input())
for _ in range(t):
    x,y,z=list(map(int,input().split()))
    a=x*y
    b=x*z
    c=b-a
    print(c)