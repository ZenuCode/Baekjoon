import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
stack = []
res = 0

def sol(x):
    global res
    if sum(stack) == k and len(stack) > 0:
        res += 1
    for i in range(x, n):
        stack.append(arr[i])
        sol(i + 1)
        stack.pop()

sol(0)
print(res)