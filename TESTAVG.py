t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if((a+b)/2>=35 and (b+c)/2>=35 and (a+c)/2>=35):
        print("PASS")
    else:
        print("FAIL")