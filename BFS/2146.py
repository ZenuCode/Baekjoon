from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] #udlr

# 땅 먼저 바꾸고 그다음에 각각 검색

for x in range(n):
    for y in range(n):
        if graph[x][y] != 0 and visited[x][y] == False:
            land_bfs(x, y)