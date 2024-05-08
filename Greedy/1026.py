import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 0

for i in range(n):
    ans += a[n - 1 - i] * b[i]

print(ans)