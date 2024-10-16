import sys
input = sys.stdin.readline

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        cnt += 1
    union(a, b)

for i in range(1, n+1):
    find(i)

numTree = len(set(parent[1:]))
print(cnt + numTree - 1)




"""
from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    visited[node] = True
    que = deque([(node, -1)])
    delNum = 0

    while que:
        curr, prev = que.popleft()
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                que.append((neighbor, curr))
            else:
                if neighbor != prev:
                    delNum += 1
    
    return delNum // 2

visited = [False] * (n+1)
numOfTrees = 0
numToDel = 0

for i in range(1, n+1):
    if not visited[i]:
        numToDel += bfs(i)
        numOfTrees += 1

if numOfTrees > 1:
    print(numToDel + numOfTrees - 1)
else:
    print(numToDel)
"""

