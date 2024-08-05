import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = float("inf")
l, r = 0, len(arr) - 1
while l < r:
    combine = arr[l] + arr[r]
    if abs(combine) < abs(res):
        res = combine

    if combine < 0:
        l += 1
    elif combine > 0 :
        r -= 1
    elif combine == 0:
        break

print(res) 