import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weight = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    weight[b] += 1

res = []
def bfs():
    que = []
    for i in range(1, n+1):
        if weight[i] == 0:
            que.append(i)

    while que:
        curr = que.pop(0)
        res.append(curr)
        for each in graph[curr]:
            weight[each] -= 1
            if weight[each] == 0:
                que.append(each)

bfs()
print(*res)