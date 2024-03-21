import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0, 0]

def paper(num, x, y):
    curr = graph[x][y]
    for i in range(x, x + num):
        for j in range(y, y + num):
            if graph[i][j] != curr:
                for a in range(3):
                    for b in range(3):
                        paper(num // 3, x + a * num // 3, y + b * num // 3)
                # 파이썬 루핑은 느린편 -> 9개만 확인하면 되니깐
                # 직접 9개를 쓰는게 휠씬 빠름
                return      
    ans[curr + 1] += 1

paper(n, 0, 0)
for i in ans:
    print(i)