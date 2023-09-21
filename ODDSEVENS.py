# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    z=a+b
    if(z%2==0):
        print("bob")
    else:
        print("alice")