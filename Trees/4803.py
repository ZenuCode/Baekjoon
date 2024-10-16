import sys
from collections import deque
input = sys.stdin.readline

def bfs(tree):
    visited[tree] = True
    que = deque([(tree, -1)])
    while que:
        curr, parent = que.popleft()
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                que.append((neighbor, curr))
                visited[neighbor] = True
            elif neighbor != parent:
                return False
    return True

caseNum = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    caseNum += 1
    res = 0
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            if bfs(i):  
                res += 1
    
    if res == 0:
        print(f"Case {caseNum}: No trees.")
    elif res == 1:
        print(f"Case {caseNum}: There is one tree.")
    else:
        print(f"Case {caseNum}: A forest of {res} trees.")