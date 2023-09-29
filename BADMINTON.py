T=int(input())
for _ in range(T):
    P=int(input())
    count=0
    for i in range(0,P+1):
        if(i%2==0):
            count=count+1
    print(count)