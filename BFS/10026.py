import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
countOne = 0
countTwo = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    visited[x][y] = True
    color = graph[x][y]

    for i in range(4):
        ux = dx[i] + x
        uy = dy[i] + y
        if 0 <= ux < n and 0 <= uy < n:
            if visited[ux][uy] == False:
                if graph[ux][uy] == color:
                    bfs(ux, uy)

for x in range(n):
    for y in range(n):
        if visited[x][y] == False:
            countOne += 1
            bfs(x, y)

visited = [[False] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if graph[x][y] == "R":
            graph[x][y] = "G"

for x in range(n):
    for y in range(n):
        if visited[x][y] == False:
            countTwo += 1
            bfs(x, y)

print(countOne, countTwo)

"""
import sys
input = sys.stdin.readline
N = int(input())
board1 = []
board2 = []
for _ in range(N):
    tmp = input().rstrip()
    board1.append(list(tmp))
    board2.append(list(tmp.replace('R','A').replace('G','A')))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,b,color):
    b[x][y] = '#'
    stack = [(x,y)]
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0<=nr<N and 0<=nc<N and b[nr][nc] == color:
                b[nr][nc] = '#'
                stack.append((nr,nc))

# 적록색약이 아닌 사람
cnt1 = 0
for i in range(N):
    for j in range(N):
        if board1[i][j] != '#':
            dfs(i,j,board1,board1[i][j])
            cnt1 += 1

# 적록색약인 사람
cnt2 = 0
for i in range(N):
    for j in range(N):
        if board2[i][j] != '#':
            dfs(i,j,board2,board2[i][j])
            cnt2 += 1

print(cnt1, cnt2)
"""