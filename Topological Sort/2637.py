import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
data = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    indegree[x] += 1

que = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)
        data[i][i] = 1

while que:
    # print(que)
    curr = que.popleft()
    # print(curr)
    # print(graph[curr])
    for target, count in graph[curr]:
        for partNum in range(1, n+1):
            data[target][partNum] += data[curr][partNum] * count
        
        # print(data[target])
        # print()
        indegree[target] -= 1
        if indegree[target] == 0:
            que.append(target)

for i in range(1, n+1):
    if data[n][i] > 0:
        print(i, data[n][i])