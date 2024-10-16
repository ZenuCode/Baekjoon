from sys import stdin
input = stdin.readline

N, K, M = map(int, input().split())

if N == 1:
    print(1)
else:
    arr = [[*map(int, input().split())] for _ in range(M)]
    hyper = [[] for _ in range(N + 1)]
    for i in range(M):
        for j in arr[i]:
            hyper[j].append(i)

    visited = [False] * (N + 1)
    visited[1] = True

    que, ans = [1], 1

    while que:
        new_que = []
        for _ in range(len(que)):
            cur = que.pop()
            if cur == N:
                print(ans)
                exit()

            for h in hyper[cur]:
                for nxt in arr[h]:
                    if not visited[nxt]:
                        new_que.append(nxt)
                        visited[nxt] = True

                arr[h] = []

        que = new_que
        ans += 1

    print(-1)
