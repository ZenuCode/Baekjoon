from collections import deque
import sys
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] #udlr

def bfs(x, y):
    que = deque([(x, y)])
    visited[x][y] = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            ux = dx[i] + x
            uy = dy[i] + y
            if visited[ux][uy] == 0:
                if 0 <= ux < row and 0 <= uy < col:
                    if graph[ux][uy] <= 0:
                        graph[x][y] -= 1
                    elif graph[ux][uy] > 0:
                        que.append((ux, uy))
                        visited[ux][uy] = 1

total = 0
go = True
while go:
    count = 0
    visited = [[0] * col for _ in range(row)]
    for x in range(row):
        for y in range(col):
            if graph[x][y] > 0 and visited[x][y] == 0:
                count += 1
                if count == 2:
                    print(total)
                    go = False
                    break
                bfs(x, y)
        if not go:
            break
    total += 1