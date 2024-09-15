import heapq
import sys

input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, ((abs(num), num)))
