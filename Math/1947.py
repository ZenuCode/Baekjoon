n = int(input())

if n < 3:
    print(n - 1)
    quit()

dp = [0 for _ in range(n + 1)]
dp[1] = 0
dp[2] = 1
dp[3] = 2

for i in range(4, n + 1):
    dp[i] = ((dp[i - 1] + dp[i - 2]) * (i - 1)) % 1000000000

print(dp[n])
