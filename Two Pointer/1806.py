import sys
arrLen, targetSum = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 1
currSum = arr[l]
res = float("inf")

while r <= arrLen:
    # print(l, r, currSum, res)
    if currSum >= targetSum:
        res = min(res, r - l)
        currSum -= arr[l]
        l += 1
    else:
        if r < arrLen:
            currSum += arr[r]
        r += 1

if res == float("inf"):
    print(0)
else:
    print(res)