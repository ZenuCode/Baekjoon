from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, ' '.join(input().split()))) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] # up down left right

que = deque([(0, 0)])

while que:
    x, y = que.popleft()
    for i in range(4):
        ux = dx[i] + x
        uy = dy[i] + y
        if 0 <= ux < n and 0 <= uy < m:
            if graph[ux][uy] == 1:
                que.append([ux, uy])
                graph[ux][uy] = graph[x][y] + 1

print(graph[n-1][m-1])