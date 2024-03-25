import sys
n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
stack = []

def backtrack():
    if len(stack) == m:
        print(*stack, sep=" ")
        return
    
    for i in range(n):
        stack.append(arr[i])
        backtrack()
        stack.pop()

backtrack()


"""
import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(input().split(), key=int)
print('\n'.join(map(' '.join, product(numbers, repeat=m))))
"""