import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
ans = []

def bfs(x, y, m):
    curr = graph[x][y]
    for i in range(x, x + m):
        for j in range(y, y + m):
            if graph[i][j] != curr:
                ans.append("(")
                bfs(x, y, m//2)
                bfs(x, y + m//2, m//2)
                bfs(x + m//2, y, m//2)
                bfs(x + m//2, y + m//2, m//2)
                ans.append(")")
                return
    if curr == 0:
        ans.append("0")
    else:
        ans.append("1")

bfs(0, 0, n)
print("".join(ans))