from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2] #clockwise from top-right

n = int(input().rstrip())
for _ in range(n):
    dim = int(input())
    cX, cY = map(int, input().split())
    tX, tY = map(int, input().split())
    graph = [[-1] * dim for _ in range(dim)]
    que = deque([[cX, cY]])
    graph[cX][cY] = 0

    while que:
        x, y = que.popleft()
        if x == tX and y == tY:
            print(graph[x][y])
            break
        
        for i in range(8):
            ux = dx[i] + x
            uy = dy[i] + y
            if 0 <= ux < dim and 0 <= uy < dim and graph[ux][uy] == -1:
                graph[ux][uy] = graph[x][y] + 1
                que.append([ux, uy])
