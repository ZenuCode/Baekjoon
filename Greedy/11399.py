import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
time, ans = 0, 0

for i in range(n):
    time += arr[i]
    ans += time

print(ans)