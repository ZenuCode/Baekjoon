import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

numMap = {}
l, r = 0, 0
res = 0

while r < len(arr):
    if arr[r] not in numMap:
        numMap[arr[r]] = 1
    else:
        check = numMap[arr[r]] + 1
        if check > k:
            res = max(res, r - l)
            while arr[l] != arr[r]:
                numMap[arr[l]] -= 1
                l += 1
            l += 1
        else:
            numMap[arr[r]] += 1
    r += 1

res = max(res, r - l)
print(res)