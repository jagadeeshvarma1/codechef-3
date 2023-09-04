# cook your dish here
for _ in range(int(input())):
    a = int(input())
    cout = 0
    while(a>0):
        a = a//5
        cout+=a
    print(cout)