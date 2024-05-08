import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))
arr.sort()
ans = 0

for each in arr:
    ans = max((n) * each, ans)
    n -= 1

print(ans)