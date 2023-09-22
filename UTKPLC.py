
T = int(input())

for _ in range(T):
    preference = input().split()
    first, second, third = preference
    offers = input().split()
    x, y = offers

    if x == first or (x == second and y == third):
        print(x)
    else:
        print(y)