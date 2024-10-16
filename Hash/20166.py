import sys
input = sys.stdin.readline
# 이 방식 보다 빠른 방법이 있어 기존꺼 참고해서 구현해봐
n, m, k = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
dx = [0, 1, 1, 1, 0, -1, -1, -1] # u, r, d, l
dy = [1, 1, 0, -1, -1, -1, 0, 1]
memo = {}

def check(word, index, row, col):
    if index == len(word):
        return 1
    if (index, row, col) in memo:
        return memo[(index, row, col)]
    
    res = 0
    for i in range(len(dx)):
        nx = (dx[i] + row) % n
        ny = (dy[i] + col) % m
        if arr[nx][ny] == word[index]:
            res += check(word, index+1, nx, ny)
    
    memo[(index, row, col)] = res
    return res

for _ in range(k):
    res = 0
    word = input().strip()
    memo.clear()
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if word[0] == arr[row][col]:
                res += check(word, 1, row, col)
    print(res)