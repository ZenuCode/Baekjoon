import sys
n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
stack = []

def backtrack(index):
    if len(stack) == m:
        print(*stack, sep=" ")
        return
    
    for i in range(index, n):
        stack.append(arr[i])
        backtrack(i + 1)
        stack.pop()

backtrack(0)