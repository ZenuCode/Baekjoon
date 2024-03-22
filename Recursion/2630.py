import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0]

def bfs(x, y, m):
    curr = graph[x][y]
    if m == 1:
        ans[curr] += 1
        return
    for i in range(x, x + m):
        for j in range(y, y + m):
            if graph[i][j] != curr:
                bfs(x, y, m//2)
                bfs(x, y+(m//2), m//2)
                bfs(x+(m//2), y, m//2)
                bfs(x+(m//2), y+(m//2), m//2)
                return
    
    ans[curr] += 1

bfs(0, 0, n)
for i in ans:
    print(i)