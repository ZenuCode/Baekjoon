import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weight = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    pdNote = list(map(int, input().split()))
    for j in range(1, pdNote[0]):
        graph[pdNote[j]].append(pdNote[j+1])
        weight[pdNote[j+1]] += 1

def topo():
    res = []
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

    return res

res = topo()
if len(res) != n:
    print(0)
else:
    print(*res)