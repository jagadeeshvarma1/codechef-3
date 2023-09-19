# cook your dish here
for i in range(int(input())):
    n,x=map(int,input().split())
    a=sorted(list(map(int,input().split())))
    print(a[n-x]-1)