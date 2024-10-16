import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
nodes = [[] for _ in range(n+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    nodes[a] = (b, c)

def rightDepth(root):
    if nodes[root][1] != -1:
        return rightDepth(nodes[root][1]) + 1
    return 1

print(2 * n - rightDepth(1) - 1)
    