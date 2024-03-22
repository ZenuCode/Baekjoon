import sys

n, m = map(int, sys.stdin.readline().split())
stack = []

def rec():
    if len(stack) == m:
        print(" ".join(map(str, stack)))
        return
    
    for i in range(1, n + 1):
        if stack and i >= stack[-1]:
            stack.append(i)
            rec()
            stack.pop()
        elif not stack:
            stack.append(i)
            rec()
            stack.pop()

rec()