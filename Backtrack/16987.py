import sys
input = sys.stdin.readline

def check(arr):
    count = 0
    for i in arr:
        if i[0] <= 0:
            count += 1
    return count

def backtrack(depth, arr):
    global ans
    if depth == n:
        ans = max(ans, check(arr))
        return
    
    if arr[depth][0] <= 0:
        backtrack(depth + 1, arr)
    else:
        broken = True
        for i in range(n):
            if depth != i and arr[i][0] > 0:
                broken = False
                arr[depth][0] -= arr[i][1]
                arr[i][0] -= arr[depth][1]
                backtrack(depth + 1, arr)
                arr[depth][0] += arr[i][1]
                arr[i][0] += arr[depth][1]
        if broken:
            backtrack(n, arr)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
backtrack(0, arr)
print(ans)