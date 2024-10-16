import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(pos):
    visited = [-1] * (n+1)
    visited[pos] = 0
    que = deque([pos])

    while que:
        pos = que.popleft()
        for each in graph[pos]:
            if visited[each] == -1:
                que.append(each)
                visited[each] = visited[pos] + 1
    
    res = 0
    maxNum = 0
    minPos = float("inf")
    for i in range(1, n+1):
        if visited[i] > maxNum:
            res = 1
            maxNum = visited[i]
            minPos = i
        elif visited[i] == maxNum:
            minPos = min(minPos, i)
            res += 1
    
    return [minPos, maxNum, res]

res = bfs(1)
print(*res)
