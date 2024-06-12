import sys
import heapq

classNum = int(input())
allTime = []
ans = []

for i in range(classNum):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    allTime.append([start, end])

allTime.sort(key=lambda x : x[0])
heapq.heappush(ans, allTime[0][1])

for i in range(1, classNum):
    if allTime[i][0] < ans[0]:
        heapq.heappush(ans, allTime[i][1])
    else:
        heapq.heappop(ans)
        heapq.heappush(ans, allTime[i][1])

print(len(ans))