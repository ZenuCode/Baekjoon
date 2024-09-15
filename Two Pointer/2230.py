import sys
input = sys.stdin.readline

def solution(A, N, M):
    left, right = 0, 0
    res = float("inf")
    while right < N:
        diff = A[right] - A[left]
        if diff < M:
            right += 1
        elif diff > M:
            res = min(diff, res)
            left += 1
        else:
            return M
    return res    

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()
res = solution(A, N, M)
print(res)
