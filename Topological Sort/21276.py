import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
names = list(map(str, input().rstrip().split()))
m = int(input())
graph = {name: [0, []] for name in names} #name, weight, child

for _ in range(m):
    a, b = map(str, input().split())
    graph[b][1].append(a)
    graph[a][0] += 1

def topo(ancestors):
    que = deque(ancestors)
    while que:
        curr = que.popleft()
        newChild = []
        for each in graph[curr][1]:
            graph[each][0] -= 1
            if graph[each][0] == 0:
                newChild.append(each)
                que.append(each)
        
        if newChild:
            graph[curr][1] = newChild
                
ancestors = []
orderName = []
for name in graph:
    if graph[name][0] == 0:
        ancestors.append(name)
    orderName.append(name)

print(len(ancestors))
print(*sorted(ancestors))

topo(ancestors)

for name in sorted(names):
    print(name, len(graph[name][1]), *sorted(graph[name][1]))