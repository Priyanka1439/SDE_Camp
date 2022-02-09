def recursive(n):
    if n <= 100:
        print(n, end=" ")
        recursive(n + 1)
n = 1
recursive(n)