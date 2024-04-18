import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    start = 0
    count = 0

    for i in range(n):
        while True:
            if start == m or a[i] <= b[start]:
                count += start
                break
            else:
                start += 1
    
    print(count)