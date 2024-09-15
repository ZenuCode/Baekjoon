import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0

for i in range(n):
    currArr = arr[:i] + arr[i + 1:]
    l, r = 0, len(currArr) - 1
    while l < r:
        check = currArr[l] + currArr[r]
        if check == arr[i]:
            res += 1
            break
        elif check > arr[i]:
            r -= 1
        elif check < arr[i]:
            l += 1

print(res)