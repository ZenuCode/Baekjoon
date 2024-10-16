import sys
from collections import deque
input = sys.stdin.readline

k = int(input())

def bfs(node):
    visited[node] = 0
    que = deque([node])

    while que:
        node = que.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = 1 - visited[node]
                que.append(neighbor)
            elif visited[neighbor] == visited[node]:
                    return False
    
    return True

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [-1] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    res = True
    for node in range(1, v+1):
        if visited[node] == -1:
            if bfs(node) == False:
                res = False
                break

    print("YES" if res else "NO")
