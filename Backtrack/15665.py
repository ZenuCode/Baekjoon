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
        if arr[i] != prev:
            stack.append(arr[i])
            prev = arr[i]
            backtrack()
            stack.pop()

backtrack()


"""
from itertools import product

n, m = map(int, input().split())
data = sorted(list(set(map(int, input().split()))))
data = list(map(str, data))

print('\n'.join(map(' '.join, product(data, repeat=m))))
"""