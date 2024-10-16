import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

res = 0
def dfs(start, end):
    visited[start] = 1
    if start == end:
        visited[end] -= 1
        return True
    for each in graph[start]:
        if visited[each[0]] == 0:
            visited[each[0]] = 1
            if dfs(each[0], end):
                visited[end] += each[1]
                return True
    
for _ in range(m):
    res = 0
    visited = [0] * (n+1)
    start, end = map(int, input().split())
    dfs(start, end)
    print(visited[end])
