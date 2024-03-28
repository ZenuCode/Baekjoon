from itertools import combinations
from collections import deque
 
 
def solution():
    flowers = 0
    spread_board = [[[0, 0] for i in range(m)] for j in range(n)]
    q = deque()
    for i in selected_r:
        x, y = candi[i]
        spread_board[x][y][1] = RED
        q.append([x, y])
    for i in selected_g:
        x, y = candi[i]
        spread_board[x][y][1] = GREEN
        q.append([x, y])

    while q:
        x, y = q.popleft()
        if spread_board[x][y][1] == FLOWER: continue
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if board[nx][ny] == 0: continue # 호수
            if spread_board[nx][ny][1] == EMPTY:
                spread_board[nx][ny][0], spread_board[nx][ny][1] = spread_board[x][y][0]+1, spread_board[x][y][1]
                q.append([nx, ny])
            elif spread_board[nx][ny][1] == RED:
                if spread_board[x][y][1] == GREEN and spread_board[x][y][0]+1 == spread_board[nx][ny][0]:
                    spread_board[nx][ny][1] = FLOWER
                    flowers += 1
            elif spread_board[nx][ny][1] == GREEN:
                if spread_board[x][y][1] == RED and spread_board[x][y][0]+1 == spread_board[nx][ny][0]:
                    spread_board[nx][ny][1] = FLOWER
                    flowers += 1
    return flowers

if __name__ == '__main__':
    n, m, g, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_flower = 0

    EMPTY = 0
    RED = 1
    GREEN = 2
    FLOWER = 3

    dxs = (0, 1, 0, -1) # 동 남 서 북
    dys = (1, 0, -1, 0)

    candi = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2: candi.append([i, j])

    for c1 in combinations(range(len(candi)), r+g):
        for c2 in combinations(range(r+g), r):
            selected_r = []
            selected_g = []
            for i in range(r+g):
                if i in c2: selected_r.append(c1[i])
                else: selected_g.append(c1[i])
            max_flower = max(max_flower, solution())
    print(max_flower)