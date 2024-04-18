from collections import deque
import sys
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(row)]
visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    visited[0][0][0] = 1
    que = deque([(0, 0, 0)])
    while que:
        x, y, wall = que.popleft()
        if x == row - 1 and y == col - 1:
            return visited[x][y][wall]
        for i in range(4):
            ux = dx[i] + x
            uy = dy[i] + y
            if 0 <= ux < row and 0 <= uy < col:
                if graph[ux][uy] == 0 and visited[ux][uy][wall] == 0:
                    visited[ux][uy][wall] = visited[x][y][wall] + 1
                    que.append((ux, uy, wall))
                elif graph[ux][uy] == 1 and wall == 0:
                    visited[ux][uy][1] = visited[x][y][wall] + 1
                    que.append((ux, uy, 1))
    return -1

print(bfs())