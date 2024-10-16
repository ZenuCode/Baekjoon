import sys
sys.setrecursionlimit(1000)

def dfs(arr, target):
    arr[target] = -2
    for i in range(len(arr)):
        if arr[i] == target:
            dfs(arr, i)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
cnt = 0

dfs(arr, k)

for j in range(len(arr)):
    if arr[j] != -2 and j not in arr:
        cnt += 1
print(cnt)