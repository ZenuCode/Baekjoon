from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * n
stack = []

def backtrack(index):
    if len(stack) == m:
        print(*stack)
        return
    
    remember = 0
    for i in range(index, n):
        if not visited[i] and remember != arr[i]:
            visited[i] = True
            stack.append(arr[i])
            remember = arr[i]
            backtrack(i + 1)
            visited[i] = False
            stack.pop()
    
backtrack(0)