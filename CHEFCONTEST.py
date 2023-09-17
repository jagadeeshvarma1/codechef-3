t = int(input())
while t > 0 :
    x,y,p,q = map(int, input().split())
    m = x + (10*p);
    f = y + (10*q)
    print("Draw" if m == f else "Chef" if m < f else "Chefina")
    t -= 1