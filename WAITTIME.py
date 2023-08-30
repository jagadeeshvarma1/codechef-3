test=int(input())

for item in range(test):
    week,day=map(int,input().split())
    print(week*7-day)