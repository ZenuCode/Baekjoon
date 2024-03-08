import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0 for _ in range(6)] for _ in range(2)]
ans = 0

for _ in range(n):
    gender, grade = map(int, input().split())
    arr[gender][grade - 1] += 1

for i in range(2):
    for j in range(6):
        ans += arr[i][j] // k
        if arr[i][j] % k:
            ans += 1

print(ans)