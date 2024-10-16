import sys
input = sys.stdin.readline

n, delNum = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
currDel = 0
res = 0

while r < len(arr):
    if arr[r] % 2 == 1:
        if currDel == delNum:
            res = max(res, r - l - delNum)
            while arr[l] % 2 == 0:
                l += 1
            l += 1
        else:
            currDel += 1
    r += 1

res = max(res, r - l - currDel)
print(res)

"""
import sys
input = sys.stdin.readline

n, delNum = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
currDel = delNum
res = 0

while r < len(arr):
    if arr[r] % 2 == 1:
        if currDel == 0:
            res = max(res, r - l - delNum)
            while arr[l] % 2 == 0:
                l += 1
            l += 1
            r += 1
        else:
            currDel -= 1
            r += 1
    else:
        r += 1

res = max(res, r - l - delNum - 1)
print(res)

"""