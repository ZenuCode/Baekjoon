import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
weight = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    weight[b] += 1

def topo():
    heap = []
    res = []
    for i in range(1, n+1):
        if weight[i] == 0:
            heapq.heappush(heap, i)
    
    while heap:
        curr = heapq.heappop(heap)
        res.append(curr)
        for each in graph[curr]:
            weight[each] -=1
            if weight[each] == 0:
                heapq.heappush(heap, each)
    
    print(*res)

topo()