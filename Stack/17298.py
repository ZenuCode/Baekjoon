import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = [-1] * n
stack = []
for i in range(n-1, -1, -1):
    temp = arr[i]

    while stack and stack[-1] <= temp:
        stack.pop()

    if stack:
        result[i] = stack[-1]
    stack.append(temp)
print(" ".join(list(map(str, result))))