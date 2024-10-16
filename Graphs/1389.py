"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    l, r = map(int, input().split())
    graph[l][r] = 1
    graph[r][l] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

minIndex = 0
minNum = float("inf")
for i in range(1, n + 1):
    dist = sum(graph[i][1:])
    if dist < minNum:
        minNum = dist
        minIndex = i

print(minIndex)

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = list([] for _ in range(n+1))

for _ in range(m):
    l, r = map(int, input().split())
    graph[r].append(l)
    graph[l].append(r)

def bfs(person):
    visited = [False] * (n + 1)
    que =[person]
    visited[person] = 0
    
    while que:
        curr = que.pop(0)
        for each in graph[curr]:
            if visited[each] == False:
                visited[each] = visited[curr] + 1
                que.append(each)

    return sum(visited)

res = []
for i in range(1, n+1):
    res.append(bfs(i))

print(res.index(min(res))+1)
