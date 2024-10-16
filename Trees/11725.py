import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

def bfs(n):
    parent = [0] * (n + 1)
    que = deque([1])
    while que:
        node = que.popleft()
        for child in edges[node]:
            if parent[child] == 0:
                parent[child] = node
                que.append(child)
    
    return parent

print(*bfs(n)[2:], sep="\n")