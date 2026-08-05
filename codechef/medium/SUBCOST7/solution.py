# cook your dish here
t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())

    if n <= 3:
        print(n * x)
    else:
        print(3 * x + (n - 3) * y)