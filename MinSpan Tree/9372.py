import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    v = n - 1
    res = 0
    for _ in range(m):
        a, b = map(int, input().split())
        a = find(a)
        b = find(b)

        if a != b:
            union(a, b)
            res += 1
            v -= 1

    print(res)

"""
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    for _ in range(M): input()
    print(N-1)

"""