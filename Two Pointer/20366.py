import sys

N = int(sys.stdin.readline())
snow = list(map(int, sys.stdin.readline().rstrip().split()))
snow.sort()
snowman = []
for i in range(N-1):
    for j in range(i + 1, N):
        snowman.append([snow[j] + snow[i], i, j])
snowman.sort(key=lambda x: x[0])

length = len(snowman)
result = float('inf')
state = 0
for i in range(length - 1):
    for j in range(i + 1, length):
        friend_cnt = snowman[j][0] - snowman[i][0]
        if friend_cnt > result:
            break
        if len({snowman[i][1], snowman[i][2], snowman[j][1], snowman[j][2]}) == 4:
            result = friend_cnt
            if result == 0:
                state = 1
    if state == 1:
        break

print(result)