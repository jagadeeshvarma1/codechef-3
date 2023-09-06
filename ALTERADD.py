for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    num=abs(a-b)
    if (num%3)!=2:
        print("yes")
    else:
        print("no")
    