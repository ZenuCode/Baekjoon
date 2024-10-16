import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, v = map(int, input().split())
paths = defaultdict(list)
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

for _ in range(m):
    l, r = map(int, input().split())
    paths[l].append(r)
    paths[r].append(l)

if not paths[v]:
    paths[v] = []

paths = {k: sorted(paths[k]) for k in paths}

dfs_res = []
def dfs(v):
    dfs_res.append(v)
    visited_dfs[v] = True
    for each in paths[v]:
        if not visited_dfs[each]:
            dfs(each)

#

bfs_res = []
def bfs(v):
    bfs_res.append(v)
    visited_bfs[v] = True
    que = deque([v])
    while que:
        path = que.popleft()
        for neighbor in paths[path]:
            if not visited_bfs[neighbor]:
                visited_bfs[neighbor] = True
                bfs_res.append(neighbor)
                que.append(neighbor)

dfs(v)
bfs(v)
print(*dfs_res)
print(*bfs_res)