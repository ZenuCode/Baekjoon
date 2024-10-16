import sys
from collections import deque
input = sys.stdin.readline
dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]

def bfs(pos, fire, graph):
    fire_que = deque(fire)
    pos_que = deque(pos)
    count = 0

    while pos_que:
        count += 1
        n = len(fire_que)
        for _ in range(n):
            x, y = fire_que.popleft()
            for i in range(4):
                ux = x + dir[i][0]
                uy = y + dir[i][1]
                if 0 <= ux < row and 0 <= uy < col:
                    if graph[ux][uy] != "#" and graph[ux][uy] != "*":
                        graph[ux][uy] = '*'
                        fire_que.append((ux, uy))
        
        n = len(pos_que)
        for _ in range(n):
            x, y = pos_que.popleft()
            for i in range(4):
                ux = x + dir[i][0]
                uy = y + dir[i][1]
                if 0 <= ux < row and 0 <= uy < col:
                    if graph[ux][uy] == '.':
                        pos_que.append((ux, uy))
                        graph[ux][uy] = '*'
                else:
                    return count
        
        return "IMPOSSIBLE"

for _ in range(int(input())):
    col, row = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(row)]
    pos, fire = (), []
    for i in range(row):
        for j in range(col):
            if graph[i][j] == '@':
                pos = (i, j)
            if graph[i][j] == '*':
                fire.append((i, j))
    
    if pos[0] == 0 or pos[1] == 0 or pos[0] == row-1 or pos[1] == col-1:
        print(1)
    else:
        print(bfs(pos, fire, graph))
