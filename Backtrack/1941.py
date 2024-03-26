from collections import deque
import sys
input = sys.stdin.readline

arr = [list(input().rstrip()) for _ in range(5)]
v = [[0] * 5 for i in range(5)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
count = 0

def bfs(x, y, yCount, sCount):
    global count
    que = deque([(x, y, yCount, sCount)])

    while que:
        x, y, yCount, sCount = que.popleft()
        if yCount + sCount == 7:
            if sCount >= 4:
                count += 1
            continue
    
        for i in range(4):
            ux = dx[i] + x
            uy = dy[i] + y
            if 0 <= ux < 5 and 0 <= uy < 5:
                v[ux][uy] = 1
                if arr[ux][uy] == "Y":
                    que.append((ux, uy, yCount + 1, sCount))
                else:
                    que.append((ux, uy, yCount, sCount + 1))
    return

for i in range(5):
    for j in range(5):
        if arr[i][j] == "S" and v[i][j] == 0:
            v[i][j] = 1
            bfs(i, j, 0, 1)

print(count)