t=int(input())
for _ in range(t):
    a,b,c,x,y,z=list(map(int,input().split()))
    e=a+b+c
    f=x+y+z
    if(e>f):
        print(1)
    else:
        print(2)