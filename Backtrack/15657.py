import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(input().split(), key=int)
print('\n'.join(map(' '.join, combinations_with_replacement(numbers, m))))


"""
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
stack = []

def dfs(start):
    if len(stack) == m:
        print(*stack)
        return
    
    for i in range(start, n):
        stack.append(arr[i])
        dfs(i)
        stack.pop()
        
dfs(0)

"""