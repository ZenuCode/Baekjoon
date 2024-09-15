import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 1, max(arr)
res = 0

while (l <= r):
    count = 0
    mid = (l + r) // 2
    
    for each in arr:
        count += (each // mid)

    if count >= m:
        res = max(res, mid)
        l = mid + 1 
    else:
        r = mid - 1

print(res)
