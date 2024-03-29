from itertools import permutations
import sys
input = sys.stdin.readline

n, m, *arr = sys.stdin.read().split()
arr.sort(key=int)
print('\n'.join(map(' '.join, dict.fromkeys(permutations(arr, int(m))))))

"""
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
stack = []
visited = [False] * n

def backtrack():
    if len(stack) == m:
        print(*stack, sep=" ")
        return
    
    remember = 0
    for i in range(n):
        if not visited[i] and remember != arr[i]:
            visited[i] = True
            stack.append(arr[i])
            remember = arr[i]
            backtrack()
            visited[i] = False
            stack.pop()

backtrack()
"""