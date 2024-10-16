import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

graph = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += b

for i in range(2, n+1):
    graph[i] = graph[i] + graph[arr[i-1]]

print(*graph[1:])