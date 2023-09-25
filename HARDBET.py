# cook your dish here
t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    print("Draw") if a < b and a < c  else print("Bob") if b < a and b < c else print("Alice")