import sys 
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    if not data[1]:
        dp[i] = data[0]
    else:
        dp[i] = max([dp[prev] for prev in data[2:]]) + data[0]

print(max(dp))