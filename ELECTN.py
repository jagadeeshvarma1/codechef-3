for _ in range(int(input())):
    n,x=map(int,input().split())
    A=list(map(int,input().split()))
    cou=0
    for i in A:
        if(i>=x):
            cou=cou+1
    print(cou)