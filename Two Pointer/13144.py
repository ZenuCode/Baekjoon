import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = 0

seen = set()
l, r = 0, 0
while r < n:
    if arr[r] not in seen:
        seen.add(arr[r])
        res += len(seen)
        r += 1
    else:
        while arr[l] != arr[r]:
            seen.remove(arr[l])
            l += 1
        seen.remove(arr[l])
        l += 1

print(res)
