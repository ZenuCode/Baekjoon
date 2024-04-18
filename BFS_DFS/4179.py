from collections import deque
import sys
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(input().rstrip()) for i in range(row)]
que = deque([])
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs():
    while que:
        x, y, check = que.popleft()
        for i in range(4):
            ux = dx[i] + x
            uy = dy[i] + y
            if check == "F":
                if 0 <= ux < row and 0 <= uy < col:
                    if graph[ux][uy] != "#" and graph[ux][uy] != "F":
                        que.append([ux, uy, "F"])
                        graph[ux][uy] = "F"
            else:
                if 0 <= ux < row and 0 <= uy < col:
                    if graph[ux][uy] != "#" and graph[ux][uy] != "F":
                        que.append([ux, uy, check + 1])
                        graph[ux][uy] = check + 1
                else:
                    return check
    return 0

if __name__ == "__main__":
    for i in range(row):
        for j in range(col):
            if graph[i][j] == "J":
                x = i
                y = j
            elif graph[i][j] == "F":
                que.append([i, j, "F"])
    
    que.append([x, y, 1])
    res = dfs()
    
    if res == 0:
        print("IMPOSSIBLE")
    else:
        print(res)
