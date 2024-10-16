import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(r):
    x, y, c = map(int, input().split())
    graph[x][y] = min(graph[x][y], c)
    graph[y][x] = min(graph[y][x], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

max_items = 0
for i in range(1, n + 1):
    total_items = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            total_items += items[j]
    max_items = max(max_items, total_items)

print(max_items)
