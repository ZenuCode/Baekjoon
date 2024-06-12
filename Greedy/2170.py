import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

left, right = arr[0][0], arr[0][1]
res = 0

for i in range(1, n):
    if right >= arr[i][1]: 
        continue
    elif arr[i][0] <= right < arr[i][1]:
        right = arr[i][1]
    elif right < arr[i][0]:
        res += right - left
        left, right = arr[i][0], arr[i][1]

res += right - left
print(res)