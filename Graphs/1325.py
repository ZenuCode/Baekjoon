import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    que = deque([start])
    count = 1 

    while que:
        curr = que.popleft()
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                que.append(neighbor)
                count += 1
    return count

max_hack = 0
result = []

for i in range(1, n + 1):
    hack_count = bfs(i)
    if hack_count > max_hack:
        max_hack = hack_count
        result = [i]
    elif hack_count == max_hack:
        result.append(i)

print(*result)
