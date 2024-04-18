import sys
from collections import deque

def main():
    drdc_knight = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (1, -2), (-1, -2))
    drdc_monkey = ((1, 0), (-1, 0), (0, 1), (0, -1))

    K = int(sys.stdin.readline())
    col, row = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
    visited = [[K+1]*(col) for _ in range(row)]
    visited[0][0] = 0

    queue = deque([(0, 0, 0, 0)])

    while queue:
        r, c, nk, cost = queue.popleft()
        if r == row-1 and c == col-1:
            print(cost)
            return

        # knight move
        if nk < K:
            for dr, dc in drdc_knight:
                if 0<=(nr:=r+dr)<row and 0<=(nc:=c+dc)<col and board[nr][nc] == 0 and visited[nr][nc] > nk+1:
                    visited[nr][nc] = nk+1
                    queue.append((nr, nc, nk+1, cost+1))
        
        # monkey move
        for dr, dc in drdc_monkey:
            if 0<=(nr:=r+dr)<row and 0<=(nc:=c+dc)<col and board[nr][nc] == 0 and visited[nr][nc] > nk:
                visited[nr][nc] = nk
                queue.append((nr, nc, nk, cost+1))
    print(-1)
    return 

main()
