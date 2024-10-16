import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1) 

for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a] = (b, c)
    if b != -1:
        parent[b] = 1
    if c != -1:
        parent[c] = 1

root = 0
for i in range(1, n+1):
    if parent[i] == 0:
        root = i
        break

nodes = []
count = 1
def dfs(node, level):
    global count
    if graph[node][0] == -1 and graph[node][1] == -1:
        nodes.append((level, count))
        count += 1
        return

    if graph[node][0] != -1:    
        dfs(graph[node][0], level+1)

    nodes.append((level, count))
    count += 1

    if graph[node][1] != -1:
        dfs(graph[node][1], level+1)
    return


dfs(root, 1)
left = [float("inf")] * (n+1)
right = [float("-inf")] * (n+1)

maxLevel = 0
for level, num in nodes:
    left[level] = min(left[level], num)
    right[level] = max(right[level], num)
    maxLevel = max(level, maxLevel)

res = [1, right[1] - left[1] + 1]
for i in range(2, maxLevel+1):
    width = right[i] - left[i] + 1
    if width > res[1]:
        res = [i, width]

print(*res)