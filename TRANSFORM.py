# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    l=["NORMAL","HUGE","SMALL"]
    print(l[x%3])