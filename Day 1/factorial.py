def fib(n, dp):
    if n <= 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return dp[n]
n = int(input("Enter the number: "))
dp = [-1 for i in range(0, n)]
print(fib(n - 1, dp))