t = int(input())
for _ in range(t):
    a, b = map(int, input().split()) 
    time_control = a + b

    if time_control < 3:
        print(1)  
    elif 3 <= time_control <= 10:
        print(2) 
    elif 11 <= time_control <= 60:
        print(3) 
    else:
        print(4)