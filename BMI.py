# cook your dish here
t=int(input())
for i in range(t):
    m,h=map(int,input().split())
    a=h*h
    b=m//a
    if b<=18:
        print(1)
    elif b>=19 and b<=24:
        print(2)
    elif b>=25 and b<=29:
        print(3)
    else:
        print(4)