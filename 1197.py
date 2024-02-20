import sys,heapq
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,cost = map(int,input().rstrip().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))
    print(graph)

print(graph)

q = [(0,1)]
visited = [False]*(N+1)
answer = 0
while q:
    print(q)
    money,start = heapq.heappop(q)
    print(money, start)
    if not visited[start]:
        print(visited)
        print(visited[start])
        visited[start] = True
        answer += money
        print(answer)
        for new_money,next in graph[start]:
            print(new_money, next, graph[start])
            if not visited[next]:
                heapq.heappush(q,(new_money,next))

print(answer)