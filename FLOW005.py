t=int(input())
for _ in range(t):
    n=int(input())
    x=[100,50,10,5,2,1]
    count=0
    
    for i in x:
        if n>=i:
            count+=n//i
            n=n%i
    print(count)