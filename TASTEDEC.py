test= int(input())

for i in range(test):
    X,Y=map(int,input().split())
    if (2*X==5*Y):
        print('Either')
    elif(2*X>5*Y):
        print('Chocolate')
    else:
        print('Candy')