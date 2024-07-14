import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
l, r = 1, max(lines)

while l <= r:
    m = (r + l) // 2
    count = sum([each // m for each in lines])

    if count >= n:
        l = m + 1
    elif count < n:
        r = m - 1

print(r)