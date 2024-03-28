# from itertools import combinations
# import sys
# input = sys.stdin.readline
# stack = []

# def backtrack(index):
#     global count
#     if len(stack) == n:
#         count += 1
#         return
#     elif n - len(stack) + index > m + 1:
#         return
    
#     for i in range(index, m + 1):
#         stack.append(i)
#         backtrack(i + 1)
#         stack.pop()

# for i in range(int(input())):
#     count = 0
#     n, m = map(int, input().split())
#     backtrack(1)
#     print(count)

import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)

"""
T = int(input())
dp = [[0] * 30 for _ in range(30)]
for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(T):
    N, M = list(map(int, input().split()))
    print (dp[N][M])
"""