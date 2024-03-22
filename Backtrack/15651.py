# import sys

# n, m = map(int, sys.stdin.readline().split())
# stack = []

# def backtrack():
#     if len(stack) == m:
#         print(" ".join(map(str, stack)))
#         return

#     for i in range(1, n + 1):
#         stack.append(i)
#         backtrack()
#         stack.pop()

# backtrack()

from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(str, range(1, n + 1)))
print("\n".join(list(map(" ".join, product(arr, repeat=m)))))

"""
A = [1,2,3]
list(itertools.product(A, repeat=2))
itertools의 product 사용법
"""