import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    l, r = map(int, input().split())
    graph[l].append(r)
    graph[r].append(l)

def dfs(index, count):
    if count == 0:
        return
    for friend in graph[index]:
        visited[friend] = 1
        dfs(friend, count-1)

visited[1] = 1
dfs(1, 2)
print(sum(visited) - 1)

