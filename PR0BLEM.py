# cook your dish here
for i in range(int(input())):
    n,m=map(int,input().split())
    if(abs(n-m)%2==0):
        print('yes')
    else:
        print('no')