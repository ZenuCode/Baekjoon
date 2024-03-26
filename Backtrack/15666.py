import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
stack = []

def backtrack():
    if len(stack) == m:
        print(*stack)
        return

    prev = 0
    for i in range(n):
        if stack and stack[-1] <= arr[i]:
            if prev != arr[i]:
                prev = arr[i]
                stack.append(arr[i])
                backtrack()
                stack.pop()
        elif not stack:
            if prev != arr[i]:
                prev = arr[i]
                stack.append(arr[i])
                backtrack()
                stack.pop()

backtrack()