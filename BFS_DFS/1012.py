import sys
input = sys.stdin.readline

def bfs(x, y):
    que = [(x,y)]
    graph[x][y] = 0

    while que:
        x, y = que.pop(0)
        for i in range(4):
            ux = dx[i] + x
            uy = dy[i] + y
            if 0 <= ux < row and 0 <= uy < col and graph[ux][uy] == 1:
                que.append([ux, uy])
                graph[ux][uy] = 0
    
    return

if __name__ == "__main__":
    n = int(input())
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for _ in range(n):
        row, col, cabbage = map(int, input().split())
        graph = [[0] * col for _ in range(row)]
        count = 0

        for _ in range(cabbage):
            curX, curY = map(int, input().split())
            graph[curX][curY] = 1
        
        for x in range(row):
            for y in range(col):
                if graph[x][y] == 1:
                    bfs(x, y)
                    count += 1
        print(count) 
