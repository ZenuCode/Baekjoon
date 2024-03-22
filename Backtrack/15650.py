import sys

n, k = map(int, sys.stdin.readline().split())
stack = []

def recur(start):
    if len(stack) == k:
        print(" ".join(map(str, stack)))
        return

    for i in range(start, n + 1):
        if stack and stack[-1] < i:
            stack.append(i)
            recur(i + 1)
            stack.pop()
        elif not stack:
            stack.append(i)
            recur(i + 1)
            stack.pop()

recur(1)