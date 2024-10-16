import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [sorted(map(int, input().split())) for _ in range(n)]
res = float("inf")

maxVal = 0
heapArr = []

for i in range(len(arr)):
    heapq.heappush(heapArr, (arr[i][0], i, 0))
    maxVal = max(maxVal, arr[i][0])

while heapArr:
    minVal, row, col = heapq.heappop(heapArr)
    res = min(res, maxVal - minVal)
    
    if col+1 < m:
        heapq.heappush(heapArr, (arr[row][col+1], row, col+1))
        maxVal = max(maxVal, arr[row][col+1])
    else:
        break

print(res)
