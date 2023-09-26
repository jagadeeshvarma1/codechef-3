t=int(input())
for _ in range(t):
    n=int(input())
    l=list(input().split())
    x,y=0,0
    for i in l:
        if i=="START38":
            x+=1
        else:
            y+=1
    print(x,y)