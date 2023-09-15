for _ in range(int(input())):
    a1,a2,b1,b2=list(map(int,input().split()))
    A=a1-a2
    B=b1-b2
    C=A+B
    if(C<0):
        print("YES")
    else:
        print("NO")