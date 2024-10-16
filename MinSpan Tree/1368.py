import sys
input = sys.stdin.readline

n = int(input())
edges = []
parent = [i for i in range(n + 1)]

for i in range(n):
    dig = int(input())
    edges.append((dig, i, n))

for i in range(n):
    connect = list(map(int, input().split()))
    for j in range(n): # for j in range(i)를 해서 반을 잘라도됨
        edges.append((connect[j], i, j))

edges.sort()

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

cnt = 0
res = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += c
        cnt += 1
        if cnt == n:
            break

print(res)
