import sys
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    path = list(map(int, input().split()))
    for j in range(i):
        graph.append((path[j], i, j))

graph.sort()

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

res = 0
v = 0
for each in graph:
    a = find(each[1])
    b = find(each[2])
    if a != b:
        union(a, b)
        res += each[0]
        v += 1
        if v == n - 1:
            break

print(res)