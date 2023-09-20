t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    min_lifetime = max(0, x * n - sum_a)
    print(min_lifetime)