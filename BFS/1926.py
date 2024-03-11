import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] # up, down, left ,right
result = []

def bfs(x, y):
    count = 1
    que = deque()
    que.append([x,y])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if graph[nx][ny] == 1:
                    count += 1
                    graph[nx][ny] = 0
                    que.append([nx, ny])

    result.append(count)
    return

for x in range(row):
    for y in range(col):
        if graph[x][y] == 1:
            graph[x][y] = 0
            bfs(x, y)

if result:
    print(len(result))
    print(max(result))
else:
    print(0)
    print(0)