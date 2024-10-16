import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(root):
    count[root] = 1 
    for each in graph[root]:
        if not count[each]:
            dfs(each)
            count[root] += count[each]
    return
    

count = [0] * (n+1)
dfs(r)

for _ in range(q):
    check = int(input())
    print(count[check])


"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(root):
    count = 0
    visited[root] = True
    if not graph[root]:
        res[root] = 1
        return 1
    
    for each in graph[root]:
        if visited[each] == False:
            visited[each] = True
            count += dfs(each)
    
    res[root] = count + 1
    return count + 1
    

res = [0] * (n+1)
visited = [False] * (n+1)
dfs(r)

for _ in range(q):
    check = int(input())
    print(res[check])
"""
