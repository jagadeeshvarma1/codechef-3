t=int(input())
for _ in range(t):
    a,b,c,d=list(map(int,input().split()))
    if(a!=c and b!=d):
        print(1)
    else:
        print(2)
        