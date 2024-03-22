import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
stack = []

def sol(depth):
    if depth == m:
        print(" ".join(map(str, stack)))
        return
    
    for i in range(n):
        if arr[i] in stack:
            continue
        stack.append(arr[i])
        sol(depth + 1)
        stack.pop()

sol(0)

"""
import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = map(str, sorted(list(map(int, input().split()))))

print('\n'.join([' '.join(i) for i in permutations(arr, m)]))
"""