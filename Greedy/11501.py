import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    maxNum = 0
    count = 0
    
    for i in range(m - 1, -1, -1):
        if maxNum < arr[i]:
            maxNum = arr[i]
        elif maxNum > arr[i]:
            count += maxNum - arr[i]
    
    print(count)