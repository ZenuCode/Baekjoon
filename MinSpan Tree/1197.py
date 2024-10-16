import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    def find(x):
        if parent[x] == x: return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b: parent[b] = a
        else: parent[a] = b

    v, e = map(int, input().split())
    parent = [i for i in range(1 + v)]
    edges = sorted([tuple(map(int, input().split())) for _ in range(e)], key=lambda x:x[2])
    res = 0

    v -= 1
    for edge in edges:
        if find(edge[0]) != find(edge[1]):
            union(edge[0], edge[1])
            res += edge[2]
            v -= 1
            if v == 0: break

    print(res)

main()