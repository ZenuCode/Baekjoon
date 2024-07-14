import sys

n = int(sys.stdin.readline())
nArr = list(map(int, sys.stdin.readline().split()))
nArr.sort()

m = int(sys.stdin.readline())
mArr = list(map(int, sys.stdin.readline().split()))

for target in mArr:
    l = 0
    r = n - 1

    while l <= r:
        m = (l + r) // 2
        if target > nArr[m]:
            l = m + 1
        elif target < nArr[m]:
            r = m - 1
        else:
            l, r = m, m
            break
    
    if l == m and r == m:
        print(1)
    else:
        print(0)