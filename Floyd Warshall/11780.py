import sys
input = sys.stdin.read

INF = float('inf')

def main():
    # 입력 처리
    data = input().splitlines()
    n = int(data[0])
    m = int(data[1])

    # 그래프와 경로 복원 배열 초기화
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    next_node = [[0] * (n + 1) for _ in range(n + 1)]  # 경로 복원용

    # 자기 자신으로 가는 거리는 0으로 초기화
    for i in range(1, n + 1):
        dist[i][i] = 0

    # 간선 정보 입력
    for i in range(2, 2 + m):
        a, b, c = map(int, data[i].split())
        if c < dist[a][b]:  # 중복 간선의 경우 더 작은 가중치만 유지
            dist[a][b] = c
            next_node[a][b] = b  # a에서 b로 바로 가는 경로

    # 플로이드-워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]  # i에서 k를 거쳐 j로 가는 경로

    # 최단 거리 출력
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] == INF:
                print(0, end=' ')
            else:
                print(dist[i][j], end=' ')
        print()

    # 경로 복원 및 출력
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] == INF or i == j:
                print(0)
            else:
                path = []
                start = i
                # 경로 복원
                while start != j:
                    path.append(start)
                    start = next_node[start][j]
                path.append(j)

                # 경로의 길이와 경로 출력
                print(len(path), *path)

if __name__ == "__main__":
    main()
