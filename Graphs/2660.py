import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

while True:
    start, end = map(int, input().split())
    if start == -1 and end == -1:
        break
    graph[start].append(end)
    graph[end].append(start)

def bfs(person):
    que = deque([person])
    visited = [-1 for _ in range(n+1)]
    visited[person] = 0
    max_depth = 0

    while que:
        currP = que.popleft()
        for friend in graph[currP]:
            if visited[friend] == -1:
                visited[friend] = visited[currP] + 1
                que.append(friend)
                max_depth = max(max_depth, visited[friend])

    return max_depth

point = [float('inf')] * (n + 1)
for person in range(1, n+1):
    point[person] = bfs(person)

min_score = min(point[1:])
res = [i for i in range(1, n+1) if point[i] == min_score]

print(min_score, len(res))
print(*res)

"""
import sys
input = sys.stdin.readline

n = int(input())
INF = float('inf')

# 거리 행렬 초기화
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0

# 친구 관계 입력받기
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dist[a][b] = 1
    dist[b][a] = 1

# 플로이드-워셜 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 각 사람의 점수 계산 (최대 거리)
scores = [0] * (n + 1)
for i in range(1, n + 1):
    scores[i] = max(dist[i][1:])  # i번 사람의 다른 모든 사람과의 거리 중 최대값

# 회장 후보 찾기
min_score = min(scores[1:])
candidates = [i for i in range(1, n + 1) if scores[i] == min_score]

# 결과 출력
print(min_score, len(candidates))
print(*candidates)
"""