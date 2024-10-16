import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

network = [[] for _ in range(n + 1)]
for _ in range(m):
    connect = list(map(int, input().split()))
    network[connect[0]].append(connect[1])
    network[connect[1]].append(connect[0])

visited = [0] * (n + 1)

def dfs(computer):
    visited[computer] = 1
    for each in network[computer]:
        if not visited[each]:
            dfs(each)

dfs(1)
print(sum(visited) - 1)
