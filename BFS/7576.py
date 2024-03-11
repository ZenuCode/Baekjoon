from collections import deque

def solution():
    count = 0
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    queue = deque([])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    ans = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        if graph[x][y] > count:
            count = graph[x][y]
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

    for i in range(n):
        for j in range(m):
            if graph[i][j]== 0:
                print(-1)
                return
    print(count - 1)

solution()