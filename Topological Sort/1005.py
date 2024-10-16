import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split()) 
    data = [0] + list(map(int, input().split())) 
    dp = [0] * (n + 1)
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    d = int(input())
    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = data[i]

    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[curr] + data[next])

            if indegree[next] == 0:
                queue.append(next)

    print(dp[d])
